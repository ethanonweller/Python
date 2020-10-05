'''
Created on Oct 4, 2020

@author: ethan
'''

from selenium import webdriver as wb
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pprint import pprint

browser = wb.Chrome(executable_path='C:/Users/ethan/Downloads/chromedriver_win32(1)/chromedriver')
browser.get('https://www.google.com/search?source=hp&ei=nnZ6X8SDO4WE9PwPj5KC4AQ&q=144hz+monitor&oq=144hz+monitor&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgsILhDHARCvARCTAjoFCC4QsQM6CAguEMcBEK8BOgsILhCxAxDHARCjAjoICAAQsQMQgwE6CAguELEDEIMBOg4ILhCxAxCDARDHARCvAVDyDligHmDsH2gBcAB4AIABiwGIAZMHkgEEMTIuMZgBAKABAaoBB2d3cy13aXqwAQY&sclient=psy-ab&ved=0ahUKEwjEyoykppzsAhUFAp0JHQ-JAEwQ4dUDCAk&uact=5')

productInfoList=WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.r4awE > span")))
prices=WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.qptdjc")))

prices_list = []
for price in prices:
    prices_list.append(price.get_attribute('innerHTML').split('<')[0].strip())
prices_list.sort(reverse=True)
pprint(prices_list)
print(len(productInfoList))
