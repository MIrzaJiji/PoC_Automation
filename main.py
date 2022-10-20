from selenium import webdriver
from time import sleep
from path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(PATH)

driver.get(URL)
print(driver.title)

tbilisi = driver.find_element(By.LINK_TEXT, "Tbilisi, Georgia")
tbilisi.click()
sleep(1)

# Print Latency
latency = driver.find_element(By.CLASS_NAME, "QarvaPlayer_Toolbox_Live_TextField.next")
print(latency.text)

# click setting
sleep(10)
# 3600 = 1 h
setting = driver.find_elements(By.CLASS_NAME, 'QarvaPlayer_Player_Button')
setting_button = setting[1]
setting_button.click()

# print qarva P version and ID
qarva_player_version = driver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Dialog-title")
print(qarva_player_version.text)
reference_Id = driver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Reference")
print(reference_Id.text)
#


sleep(10)
driver.quit()
