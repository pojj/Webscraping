from selenium import webdriver
import time

driver = webdriver.Chrome("E:/William is cool/PythonProjects/programs/webscraping/chromedriver.exe")
driver.get("https://monkeytype.com/")

time.sleep(5)


while True:
    words = driver.find_element_by_xpath("/html/body/div[26]/div/div[2]/div[2]/div[1]/div[7]/div[3]").text
    active = driver.find_element_by_class_name("word.active").text
    words = words[words.find(active)::].replace("\n", " ") + " "

    driver.find_element_by_xpath("/html/body").send_keys(words)



'''
while True:
    word = driver.find_element_by_class_name("word.active").text
    driver.find_element_by_xpath("/html/body").send_keys(" " + word + " ")
    # I REALLY HAVE ZERO FKING IDEA WHY I NEED TWO SPACES

'''
