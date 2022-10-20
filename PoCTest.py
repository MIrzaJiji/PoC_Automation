from selenium import webdriver
from time import sleep
from path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import *

switchServer()

## qarva part
qarvaDriver = webdriver.Chrome(PATH)
# 1

run_silk_info()
# 2
sleep(5)

# 3

# 4-5
settings_click()

return_reference()

return_player_version()

# 6
# qarvaDriver.quit()

# grafana part

sleep(300)

print("time to check network")

sleep(150)
# sleep(2)


7
run_grafana()

# 8

authorization_grafana()

# 9

sleep(180)
# sleep(2)
# 10
filter_by_reference(return_reference())

# 11
filter_by_session()

# 13
# print(return_reference())
# print(return_player_version())


return_session_start_time()

return_session_duration()
return_start_latency()
return_playback_start_time()

return_final_latency()
change_chanel()

##

print("spike time")
sleep(150)
qarvaDriver.quit()

##
return_bitrate_switch_count()

return_interruptions()

# sleep(10)
# driver.quit()
