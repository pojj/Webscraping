from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("E:\William is cool\programs\webscraping\chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSftxNqU8_nran3W6AAFdVj-HJuZKRyMcNzeKyyHblSdfkLP7Q/viewform")
time.sleep(3)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div').click()