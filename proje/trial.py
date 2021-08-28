from selenium import webdriver

import time

driver=webdriver.Firefox()

url="https://instagram.com"


driver.get(url)
time.sleep(1)
us=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")

us.send_keys("crashjj62478")

passs=driver.find_element_by_name("password")


passs.send_keys("1234")

gir=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")

gir.click()