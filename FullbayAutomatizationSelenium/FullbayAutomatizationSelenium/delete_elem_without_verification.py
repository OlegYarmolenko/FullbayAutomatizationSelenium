import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()


browser.get('https://app.fullbay.com')

searchBar = browser.find_element_by_id('email')
searchBar.send_keys('mason@rpmdispatch.com')
passwordBar = browser.find_element_by_name('password')
passwordBar.send_keys('25c50t45')
passwordBar.send_keys(Keys.ENTER)
#masonBlock = browser.find_element_by_link_text('Mason Supotnitskiy (18082)')
#masonBlock.click()
masonBlock = browser.find_element_by_css_selector('li.dropdown')
masonBlock.click()
masonBlock2 = browser.find_element_by_link_text('Services & PMs')
masonBlock2.click()


i: int = 0
while i < 65:
    servicesAndPMs = browser.find_element_by_css_selector('th:nth-child(1)')
    servicesAndPMs.click()
    findCoronado = browser.find_element_by_css_selector(
    '#dataTableEntityComponentSystemCorrection > tbody > tr:nth-child(19)')
    findCoronado.click()
    time.sleep(0.5)
    findButtonDelete = browser.find_element_by_css_selector('button.btn.btn-danger')
    findButtonDelete.click()
    time.sleep(0.5)
    browser.switch_to.alert.accept()
    time.sleep(0.5)
    browser.switch_to.alert.accept()
    print(i)
    i = i + 1
