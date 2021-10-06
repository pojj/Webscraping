from selenium import webdriver
import time

driver = webdriver.Chrome("E:\William is cool\PythonProjects\programs\webscraping\chromedriver.exe")
driver.get("https://humanbenchmark.com/tests/verbal-memory")

time.sleep(3)

words = []
counter = 0

driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[4]/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div")

while True:
    counter += 1
    word = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div").text

    if word in words:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]").click()

    else:
        words.append(word)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[2]").click()

    if counter == 100000:
        print(crashme)
