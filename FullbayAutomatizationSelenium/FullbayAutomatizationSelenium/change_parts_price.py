import selenium
import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

workbook = xlrd.open_workbook("PartsTestnew.xlsx")

worksheet = workbook.sheet_by_index(0)

print("the value at row 1 and column 1 is : {0}".format(worksheet.cell(0, 1).value))

browser = webdriver.Chrome()

browser.get('https://app.fullbay.com')

searchBar = browser.find_element_by_id('email')
searchBar.send_keys('mason@rpmdispatch.com')
passwordBar = browser.find_element_by_name('password')
passwordBar.send_keys('25c50t45')
passwordBar.send_keys(Keys.ENTER)
truckShop = browser.find_element_by_css_selector(
    "#leftNavMenu > div:nth-child(2) > div.dropdown > div > span:nth-child(1)")
truckShop.click()
truckShopDropDown = browser.find_element_by_css_selector(
    "#leftNavMenu > div:nth-child(2) > div.dropdown.open > ul > li:nth-child(2)")
truckShopDropDown.click()
PartsButton = browser.find_element_by_css_selector("#leftNavMenu > div:nth-child(6) > div")
PartsButton.click()
inventoryBtn = browser.find_element_by_css_selector(
    "#rightColumn > div.panel.panel-default > div.panel-body > ul > li:nth-child(3) > a")
inventoryBtn.click()

i: int = 0
zeroColumnForPartsName: int = 0
firstColumnForPartsPrice: int = 1

numForParts: int = 686
# numForPartsName: int = 0
# numForPartsPrice: int = 0

while i < 32:

    partsName = worksheet.cell(numForParts, zeroColumnForPartsName).value
    if type(partsName) == float:
        partsName = int(partsName)
    partsPrice: str = worksheet.cell(numForParts, firstColumnForPartsPrice).value
    time.sleep(1)
    inventorySearchBar = browser.find_element_by_css_selector("#searchAllDataTables")
    inventorySearchBar.send_keys(str(partsName))
    time.sleep(1)
    try:
        firstItemOfPartsList = browser.find_element_by_css_selector("#dataTable > tbody > tr > td:nth-child(2)")
        firstItemOfPartsList.click()
        browser.switch_to.window(browser.window_handles[1])
    except:
        print("Didn't find the part's name")

    try:
        averageCostBtn = browser.find_element_by_css_selector(
            "body > table > tbody > tr > td > div:nth-child(3) > div.panel-body > table > tbody > tr:nth-child(6) > td.right > button")
    except selenium.common.exceptions.NoSuchElementException:
        print(partsName, partsPrice)


    try:
        averageCostBtn.click()

        time.sleep(0.5)

        averageCostInput = browser.find_element_by_css_selector("#averageCost")
        averageCostInput.send_keys(str(partsPrice))

        time.sleep(1)

        submitBtn = browser.find_element_by_css_selector("#myForm > button")

        submitBtn.click()
        time.sleep(0.5)

        browser.switch_to.alert.accept()
        time.sleep(0.5)
    except:
        print("Didn't find average cost modify button")

    try:
        if browser.window_handles[1]:
            browser.close()
    except IndexError:
        print("Program do not find another window, so continue to work")
    browser.switch_to.window(browser.window_handles[0])

    inventorySearchBar = browser.find_element_by_css_selector("#searchAllDataTables")
    inventorySearchBar.clear()

    print(numForParts)
    i = i + 1
    numForParts = numForParts + 1
