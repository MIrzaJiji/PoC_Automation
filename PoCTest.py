from selenium import webdriver
from time import sleep
from path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import *

## qarva part
qarvaDriver = webdriver.Chrome(PATH)
# 1
qarvaDriver.get(URL_tbilisi)
print(qarvaDriver.title)

# 2
sleep(5)

# 3

# 4-5
setting = qarvaDriver.find_elements(By.CLASS_NAME, 'QarvaPlayer_Player_Button')
setting_button = setting[1]
setting_button.click()

qarva_player_version = qarvaDriver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Dialog-title").text
reference_Id = qarvaDriver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Reference").text
reference_Id = reference_Id[14:30]
print(reference_Id)

# 6
# qarvaDriver.quit()

# grafana part

sleep(300)

print("time to check network")

sleep(150)
# sleep(2)


7
driverGraf = webdriver.Chrome(PATH)
driverGraf.get(URLGraf)

# 8
graf_user = driverGraf.find_element(By.NAME, "user")
graf_password = driverGraf.find_element(By.NAME, "password")

graf_user.send_keys(grafanaUser)
graf_password.send_keys(grafanaPass)
graf_LogIn_button = driverGraf.find_element(By.CLASS_NAME, "css-14g7ilz-button")
graf_LogIn_button.click()

# 9

sleep(180)
# sleep(2)
# 10
driverGraf.find_element(By.XPATH,
                        '//*[@id="1"]/section/div[2]/div/div/div[1]/div/div[1]/div/div[2]/span/div').click()
driverGraf.find_element(By.CLASS_NAME, "css-yn255a-input-input").send_keys(reference_Id)
# driverGraf.find_element(By.CLASS_NAME, "css-yn255a-input-input").send_keys("650cd4fa6e1d3683")  # test
driverGraf.find_elements(By.CLASS_NAME, "css-yu4292-filterListRow")[0].click()
driverGraf.find_element(By.XPATH,
                        "/html/body/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]").click()

# 11
session_id = driverGraf.find_element(By.CLASS_NAME, 'css-1w5pd0q')

# 12
driverGraf.find_element(By.CLASS_NAME, "css-5t1gy9").click()

driverGraf.find_element(By.CLASS_NAME, "gf-form-input").send_keys(session_id.text, Keys.RETURN)

# 13
print(reference_Id)
print(qarva_player_version)

session_start_time = driverGraf.find_elements(By.CLASS_NAME, "css-1w5pd0q")[5]
print("session start time: ", session_start_time.text, "\n")

session_duration = driverGraf.find_elements(By.CLASS_NAME, "css-1w5pd0q")[6]
print("session duration", session_duration.text, "\n")

start_latency = driverGraf.find_element(By.XPATH,
                                        "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[5]/div/section/div[2]/div/div[1]").text
print(start_latency, "\n")

playback_start_time = driverGraf.find_element(By.XPATH,
                                              "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[1]").text
print(playback_start_time, "\n")

final_latency = driverGraf.find_element(By.XPATH,
                                        "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[5]/div/section/div[2]/div/div[2]").text
print(final_latency, "\n")

##
secondChanel = qarvaDriver.find_element(By.CLASS_NAME, "Demo_Connected_Channel")
secondChanel.click()
print("spike time")
sleep(150)
qarvaDriver.quit()

##
bitrate_switch_count = driverGraf.find_element(By.XPATH,
                                               "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[7]/div/section/div[2]/div/div[1]").text
print(bitrate_switch_count, "\n")

interruptions_count = driverGraf.find_element(By.XPATH,
                                              "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[7]/div/section/div[2]/div/div[2]").text
print(interruptions_count, "\n")

interruptions_sum = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[5]").text
print(interruptions_sum, "\n")

interruptions_min = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[2]").text
print(interruptions_min, "\n")

interruptions_max = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[4]").text
print(interruptions_max, "\n")

interruptions_avg = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[3]").text
print(interruptions_avg, "\n")

channel_change_time = driverGraf.find_element(By.XPATH,
                                              "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[6]/div/section/div[2]/div").text
print(channel_change_time, "\n")

# sleep(10)
# driver.quit()
