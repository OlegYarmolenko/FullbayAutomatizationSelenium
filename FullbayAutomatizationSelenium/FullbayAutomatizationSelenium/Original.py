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

workbook = xlrd.open_workbook("part_qty.xlsx")
worksheet = workbook.sheet_by_index(0)


workbook_wt = xlsxwriter.Workbook('Newparts_list.xlsx')
worksheet_wt = workbook_wt.add_worksheet()

i=0
parttest="sdfsdf"
row_wt=0
col_wt=0
text_wt=55
partstame=1

while i<10:
    worksheet_wt.write(row_wt, col_wt, text_wt)
    row_wt= row_wt+1
    text_wt= text_wt+1
    i= i+1




browser = webdriver.Chrome()
browser.get('https://app.fullbay.com')

searchBar = browser.find_element_by_id('email')
searchBar.send_keys('russel@rpmdispatch.com')
passwordBar = browser.find_element_by_name('password')
passwordBar.send_keys('12345678')
passwordBar.send_keys(Keys.ENTER)
browser.get('https://app.fullbay.com/office/part/indexEntityLocationPart.html')
searchPartBar = browser.find_element_by_id('searchAllDataTables')

i=0
rowx = 0
colx = 0
while i < 5000:
    SheetPartName = worksheet.cell(rowx,colx).value
    searchPartBar.send_keys(SheetPartName)
    part_in_list = browser.find_element_by_css_selector("#dataTable > tbody > tr:nth-child(1) > td:nth-child(2)")

    if part_in_list.text == SheetPartName:
        part_in_list.click()
        browser.switch_to.window(browser.window_handles[1])
        in_stock = browser.find_element_by_css_selector("body > table > tbody > tr > td > div:nth-child(3) > div.panel-body > table > tbody > tr:nth-child(8) > td.right > a")
        in_transit_value = int(browser.find_element_by_css_selector("body > table > tbody > tr > td > div:nth-child(3) > div.panel-body > table > tbody > tr:nth-child(9) > td.right").text)
        in_stock.click()

        try:
            second_location = browser.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr[2]/td[4]/input")
        except:

            min_qty = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr[1]/td[4]/input")
            min_qty.clear()
            min_qty.send_keys("0")

            max_qty = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/span/div/form/div[1]/table/tbody/tr[1]/td[5]/input")
            max_qty.clear()
            max_qty.send_keys("0")

            submit_btn = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/span/div/form/div[2]/div[2]/button[2]")
            submit_btn.click()

            browser.close()
            browser.switch_to.window(browser.window_handles[0])
        else:
            worksheet_wt.write(row_wt, col_wt, text_wt)






