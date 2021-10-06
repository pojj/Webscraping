from selenium import webdriver
import sys
import time
driver=webdriver.Chrome("E:\William is cool\programs\Other\webscraping\chromedriver.exe")
#driver.get("https://www.walmart.ca/en");
driver.get("https://www.walmart.ca/en/scheduled-shopping/delivery");
"""driver.find_element_by_class_name("e1xmck040").click()
time.sleep(3)
driver.find_element_by_link_text("Book a Slot").click()
time.sleep(3)
driver.find_element_by_class_name("css-1z0ajcp.ekclamd2").click()
time.sleep(3)"""
abc=True
while abc==True:
    time.sleep(2)
    driver.find_element_by_id("firstName").send_keys("banana")
    driver.find_element_by_id("lastName").send_keys("banana")
    driver.find_element_by_id("address1").send_keys("banana")
    driver.find_element_by_id("city").send_keys("Surrey")
    driver.find_element_by_id("province").send_keys("British Columbia")
    driver.find_element_by_id("postalCode").send_keys("v3n0s5")
    driver.find_element_by_id("phoneNumber").send_keys("1111111111")
    driver.find_element_by_class_name("css-1h72fhx.edzik9p0").click()
    time.sleep(4)
    while True:
        for a in range(1,7):
            for b in range(1,4):
                if driver.find_element_by_id("ts-row-"+str(a)+"-col-"+str(b)).text!="Not Available":
                    driver.find_element_by_id("ts-row-"+str(a)+"-col-"+str(b)).click()
                    abc=False
                    sys.exit()
        if driver.find_element_by_id("next-slots").is_enabled()==True:
            driver.find_element_by_id("next-slots").click()
            time.sleep(5)
        else:break
    time.sleep(5)
    if abc==True:
        driver.refresh()
    else: break
