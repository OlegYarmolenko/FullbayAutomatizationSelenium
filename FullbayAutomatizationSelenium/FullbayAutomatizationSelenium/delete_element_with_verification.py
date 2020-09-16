import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# i: int = 0
# while i <= 4:
#     print(i)
#     i = i + 1

# print("Hello World")
# cool = "FUEL INJECTORS: One"
# x = ':' in cool
# if x==True:
#     print("First variant")
# else:
#     print("Second variant")


browser = webdriver.Chrome()

browser.get('https://app.fullbay.com')

searchBar = browser.find_element_by_id('email')
searchBar.send_keys('mason@rpmdispatch.com')
passwordBar = browser.find_element_by_name('password')
passwordBar.send_keys('25c50t45')
passwordBar.send_keys(Keys.ENTER)
# masonBlock = browser.find_element_by_link_text('Mason Supotnitskiy (18082)')
# masonBlock.click()
masonBlock = browser.find_element_by_css_selector('li.dropdown')
masonBlock.click()
masonBlock2 = browser.find_element_by_link_text('Services & PMs')
masonBlock2.click()

btnComponent = browser.find_element_by_css_selector('th:nth-child(1)')
btnComponent.click()

i: int = 0
numberOfElement = 23
numberOfElementString = str(numberOfElement)
while i < 143:

    element = browser.find_element_by_css_selector(
        "#dataTableEntityComponentSystemCorrection > tbody > tr:nth-child(" + numberOfElementString + ") > td:nth-child(3)")

    textFromElement = element.text
    findingSymbol = 'PM' in textFromElement
    # findElectrical = "ELECTRICAL" in textFromElement
    # findInspectionTruck = "Inspection (Truck)" in textFromElement

    #findComputerDiagnostic = "Computer Diagnostic" in textFromElement
    #findServiceAPU = "Service APU" in textFromElement
    #findTestRunL = "Test run(long)" in textFromElement
    #findTestRunS = "Test run(short)" in textFromElement
    #if not findComputerDiagnostic and not findServiceAPU and not findTestRunL and not findTestRunS:

    if not findingSymbol:
        element.click()
        time.sleep(0.5)
        findButtonDelete = browser.find_element_by_css_selector('button.btn.btn-danger')
        findButtonDelete.click()
        time.sleep(0.5)
        browser.switch_to.alert.accept()
        time.sleep(0.5)
        browser.switch_to.alert.accept()
        btnComponent = browser.find_element_by_css_selector('th:nth-child(1)')
        btnComponent.click()
        print(i)
        i = i + 1
    else:
        numberOfElement = numberOfElement + 1
        numberOfElementString = str(numberOfElement)
        i = i + 1
