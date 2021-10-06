from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
def check(xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        return False
    return True
driver=webdriver.Chrome("E:\William is cool\programs\Other\webscraping\chromedriver.exe")
driver.get("https://app.schoology.com/login")
time.sleep(3)
driver.find_element_by_id("edit-mail").send_keys("Williambsong@gmail.com")
driver.find_element_by_id("edit-pass").send_keys("")
driver.find_element_by_id("edit-submit").click()
time.sleep(3)
driver.find_element_by_xpath('//span[@class="_1D8fw"]').click()
time.sleep(1)
driver.find_element_by_xpath('//article/a[@href="/course/2348232816"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div/a[@href="/course/2348232816/materials?f=181131490"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div/a[@href="/assignment/2497817316"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div/a[@href="/assignment/2497817316/assessment"]').click()
time.sleep(3)
#driver.find_element_by_id("edit-submit-1").click()
driver.find_element_by_id("edit-resume-1").click()
time.sleep(3)
'''
while True:
    if check('//label/input[@value="0"]')==True:
        driver.find_element_by_xpath('//label/input[@value="0"]').click()
    if check('//label/input[@value="t"]')==True:
        driver.find_element_by_xpath('//label/input[@value="t"]').click()
    if check('//input[@value="Next Page"]')==True:
        driver.find_element_by_xpath('//input[@value="Next Page"]').click()
    if check('//input[@value="Review Answers"]')==True:
        driver.find_element_by_xpath('//input[@value="Review Answers"]').click()
        break
    time.sleep(1)
'''
while True:
    if check('//label/input[@value="0"]')==True:
        time.sleep(2)
        driver.find_element_by_xpath('//label/input[@value="0"]').send_keys(Keys.ENTER)
    elif check('//label/input[@value="t"]')==True:
        time.sleep(2)
        driver.find_element_by_xpath('//label/input[@value="t"]').send_keys(Keys.ENTER)
    if check('//span/input[@value="Submit"]')==True:
        break
    time.sleep(2)
time.sleep(2)
driver.find_element_by_xpath('//input[@value="Yes"]').click()
