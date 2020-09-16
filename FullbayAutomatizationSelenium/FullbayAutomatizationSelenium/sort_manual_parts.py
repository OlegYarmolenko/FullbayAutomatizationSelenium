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

workbook = xlrd.open_workbook("part_qty.xlsx")
worksheet = workbook.sheet_by_index(0)

workbook_wt = xlsxwriter.Workbook('Changed_parts_qty.xlsx')
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

while i < 4505:
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
                in_stock = browser.find_element_by_css_selector(
                    "body > table > tbody > tr > td > div:nth-child(3) > div.panel-body > table > tbody > tr:nth-child(8) > td.right > a")
                in_stock.click()
            except Exception as e:
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
                worksheet_wt.write(rowx, 2, str(e))
            try:
                wait = WebDriverWait(browser, 10)
                close_btn = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[1]")))
                close_btn = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[1]")

                second_location = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr[2]/td[4]/input")
                worksheet_wt.write(rowx, colx, SheetPartName)
                worksheet_wt.write(rowx, 1, "need to do manually")

            except:
                worksheet_wt.write(rowx, colx, SheetPartName)
                worksheet_wt.write(rowx, 1, "Can be automized")

            wait = WebDriverWait(browser, 10)
            close_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[1]")))
            close_btn = browser.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[1]")
            close_btn.click()

            browser.close()
            browser.switch_to.window(browser.window_handles[0])

        else:
            worksheet_wt.write(rowx, colx, SheetPartName)
            worksheet_wt.write(rowx, 1, "need to do manually")


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
