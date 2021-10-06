from selenium.webdriver import Chrome
import time
driver = Chrome("E:/William is cool/PythonProjects/programs/webscraping/chromedriver.exe")
driver.get("https://www.mcrpg.com/kohi-click-test/")
button = driver.find_element_by_class_name("btn-default")
time.sleep(3)
while True:
    button.click()
