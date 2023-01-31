import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)
driver.find_element("name", "username").clear()
driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").clear()
driver.find_element("name", "password").send_keys("admin123")

time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

real_title = driver.title
exp_title = "OrangeHRM"

if real_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

time.sleep(5)

driver.close()