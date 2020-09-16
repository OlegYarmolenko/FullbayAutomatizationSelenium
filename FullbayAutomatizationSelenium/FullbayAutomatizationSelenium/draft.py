import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# workbook = xlrd.open_workbook("PartsTestnew.xlsx")
# worksheet = workbook.sheet_by_index(0)
#
# #cell__value = "{}".format(worksheet.cell(0, 0).value)
#
# cell__value: str = worksheet.cell(0, 0).value
# print(cell__value)
# print(type(cell__value))
#
# bIf = type(cell__value) == float
# print(bIf)
#
# if bIf:
#     cell__value = int(cell__value)
#     print(type(cell__value))
#     print(cell__value)
try:
    x = int(input())
except ValueError:
    print("Vi vveli ne chislo")
    x = 0
else:
    print("Vsio otlichno")
finally:
    print("Vipolyaem v libom sluchae")



y = int(input())

try:
    res = x / y
except ZeroDivisionError:
    print("Vi vveli  nol'")
    res = 0

print("prodolzhaem programu")
print(res)