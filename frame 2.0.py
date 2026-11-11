import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.switch_to.frame("singleframe")

invalue=driver.find_element(By.XPATH,"/html/body/section/div/div/div/input")
invalue.send_keys("Go to Gym")
time.sleep(2)

driver.switch_to.default_content()
