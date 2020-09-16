import selenium
import xlrd
import xlwt
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlsxwriter
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.support.ui import Select

workbook = xlrd.open_workbook("Can_be_automized_parts.xlsx")
worksheet = workbook.sheet_by_index(0)

workbook_wt = xlsxwriter.Workbook('Min_Max_qty.xlsx')
worksheet_wt = workbook_wt.add_worksheet()

browser = webdriver.Chrome()
browser.get('https://app.fullbay.com')

searchBar = browser.find_element_by_id('email')
searchBar.send_keys('rick@rpmdispatch.com')
passwordBar = browser.find_element_by_name('password')
passwordBar.send_keys('123456789')
passwordBar.send_keys(Keys.ENTER)
browser.get('https://app.fullbay.com/office/part/indexEntityLocationPart.html')
searchPartBar = browser.find_element_by_id('searchAllDataTables')

start_time = datetime.now()

i = 0
rowx = 0
colx = 0

while i < 4081:
    print(i)
    try:
        SheetPartName = worksheet.cell(rowx, colx).value
        if type(SheetPartName)==float:
            SheetPartName = str(int(SheetPartName))
        searchPartBar.send_keys(SheetPartName)
        try:
            part_in_list = browser.find_element_by_css_selector(
                "#dataTable > tbody > tr:nth-child(1) > td:nth-child(2)")
        except Exception as e:
            print(e)

        if part_in_list.text == SheetPartName:
            part_in_list.click()
            browser.switch_to.window(browser.window_handles[1])
            try:
                in_stock = browser.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td/div[2]/div[2]/table/tbody/tr[8]/td[3]/a")
                in_stock.click()
            except Exception as e:
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
                worksheet_wt.write(rowx, 2, str(e))


            try:
                wait = WebDriverWait(browser, 10)
                Min_Qty_wait = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr/td[4]/input")))
                Max_Qty_wait = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr/td[5]/input")))

                Min_Qty = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr/td[4]/input")
                Max_Qty  = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr/td[5]/input")

                Min_Qty.clear()
                Max_Qty.clear()

                Min_Qty.send_keys(0)
                Max_Qty.send_keys(0)

                submit_btn_wait = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[2]")))
                submit_btn = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[2]")
                submit_btn.click()


                in_transit_wait = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/table/tbody/tr/td/div[2]/div[2]/table/tbody/tr[9]/td[3]")))
                in_transit = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div[2]/table/tbody/tr[9]/td[3]")
                in_stock = browser.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td/div[2]/div[2]/table/tbody/tr[8]/td[3]/a")
                if in_stock.text == in_transit.text:

                    edit_btn_wait = wait.until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/button[1]")))
                    edit_btn = browser.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/button[1]")
                    edit_btn.click()

                    select_field_wait = wait.until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/table/tbody/tr/td/div[2]/div[2]/form/div[1]/label/select")))
                    select = Select(browser.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div[2]/form/div[1]/label/select"))
                    select.select_by_value("Inactive")

                    save_btn_wait = wait.until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/table/tbody/tr/td/div[2]/div[2]/form/div[4]/button[1]")))
                    save_btn =  browser.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div[2]/form/div[4]/button[1]")
                    save_btn.click()

                    worksheet_wt.write(rowx, 2, "Changed Status => Inactive")

                worksheet_wt.write(rowx, colx, SheetPartName)
                worksheet_wt.write(rowx, 1, "Changed min_max QTY")

            except Exception as e:
                worksheet_wt.write(rowx, colx, SheetPartName)
                worksheet_wt.write(rowx, 1, str(e))



            browser.close()
            browser.switch_to.window(browser.window_handles[0])

        else:
            worksheet_wt.write(rowx, colx, SheetPartName)
            worksheet_wt.write(rowx, 1, "name doesn't match in searchbar")


    except Exception as e:
        print(e)
        print(SheetPartName)
        worksheet_wt.write(rowx, colx, SheetPartName)
        worksheet_wt.write(rowx, 1, str(e))
    try:
        searchPartBar.clear()
        rowx = rowx + 1
        i = i + 1
    except Exception as e:
        print(e)
        print(SheetPartName)
        worksheet_wt.write(rowx, colx, SheetPartName)
        worksheet_wt.write(rowx, 1, str(e))

workbook_wt.close()
print(datetime.now() - start_time)
