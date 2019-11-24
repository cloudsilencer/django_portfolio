import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = maximize.window()

# test scenario 1
driver.get("http://localhost:8000/blog/2")
elem = driver.find_element_by_name("author")
elem.clear()
elem.send_keys("Li Yun")

elem = driver.find_elements(By.XPATH, '//button')
elem.send_keys(Keys.RETURN)

# test scenario 2
driver.get("http://localhost:8000/blog/2")
elem = driver.find_element_by_name("body")
elem.clear()
elem.send_keys("This is great!")

elem = driver.find_elements(By.XPATH, '//button')
elem.send_keys(Keys.RETURN)






