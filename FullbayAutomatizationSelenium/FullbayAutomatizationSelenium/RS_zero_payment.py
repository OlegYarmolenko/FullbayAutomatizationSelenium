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
browser.get('https://app.fullbay.com/office/customer/indexNew.html')

wait = WebDriverWait(browser, 10)
change_shop_to_frs = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[7]/div[2]/div/div[2]/button")))
change_shop_to_frs = browser.find_element_by_xpath("/html/body/div[7]/div[2]/div/div[2]/button")
change_shop_to_frs.click()

change_shop_to_frs = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[7]/div[2]/div/div[2]/ul/li[3]/a")))
change_shop_to_frs = browser.find_element_by_xpath("/html/body/div[7]/div[2]/div/div[2]/ul/li[3]/a")
change_shop_to_frs.click()

find = True

while find == True:
    first_invoice = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[7]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[1]")))
    first_invoice = browser.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[1]")
    first_invoice.click()

    create_inv_btn = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[7]/div[3]/div[2]/div[4]/form/div[7]/div[3]/input")))
    create_inv_btn = browser.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div[2]/div[4]/form/div[7]/div[3]/input")
    create_inv_btn.click()



    close_btn = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/span[2]")))
    close_btn = browser.find_element_by_xpath(
        "/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/span[2]")

    close_btn.click()



