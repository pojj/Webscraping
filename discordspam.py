from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("E:\William is cool\PythonProjects\programs\webscraping\chromedriver.exe")
driver.get('https://discord.com/channels/@me/755119133477175358')
time.sleep(3)

driver.find_element_by_name('email').send_keys("williambsong@gmail.com")
driver.find_element_by_name('password').send_keys("")
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(10)
number=1

while True:
    prime=True
    number+=1
    time.sleep(0.2)
    for i in range(2,number):  
       if (number % i) == 0:  
           prime=False
           break  
    if prime==True:
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[3]/div[2]').send_keys(str(number))
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div[3]/div').send_keys(Keys.ENTER)
