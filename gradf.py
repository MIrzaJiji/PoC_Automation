from selenium import webdriver
from time import sleep
from path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(PATH)

driver.get(URLGraf)

print(driver.title)

# driver.quit()
