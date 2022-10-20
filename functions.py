from selenium import webdriver
from time import sleep
from path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

qarvaDriver = webdriver.Chrome(PATH)
driverGraf = webdriver.Chrome(PATH)


def switchServer():
    print("switch server:\n1)tbilisi\n2)dublin\n3)sydney\n4)roaming\n")
    x = int(input())
    if x == 1:
        URL = URL_tbilisi

    elif x == 2:
        URL = URL_dublin

    elif x == 3:
        URL = URL_sydney

    elif x == 4:
        URL = URL_roaming

    else:
        switchServer()
    return URL


def run_silk_info():
    qarvaDriver.get(switchServer())
    print(qarvaDriver.title)


def settings_click():
    setting = qarvaDriver.find_elements(By.CLASS_NAME, 'QarvaPlayer_Player_Button')
    setting_button = setting[1]
    setting_button.click()


def return_reference():
    reference_Id = qarvaDriver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Reference").text
    reference_Id = reference_Id[14:30]
    return reference_Id
    # print(reference_Id)


def return_player_version():
    qarva_player_version = qarvaDriver.find_element(By.CLASS_NAME, "QarvaPlayer_Player_Settings_Dialog-title").text
    return qarva_player_version


def run_grafana():
    driverGraf = webdriver.Chrome(PATH)
    driverGraf.get(URLGraf)


def authorization_grafana():
    graf_user = driverGraf.find_element(By.NAME, "user")
    graf_password = driverGraf.find_element(By.NAME, "password")
    graf_user.send_keys(grafanaUser)
    graf_password.send_keys(grafanaPass)
    graf_LogIn_button = driverGraf.find_element(By.CLASS_NAME, "css-14g7ilz-button")
    graf_LogIn_button.click()


def filter_by_reference(reference_id):
    driverGraf.find_element(By.XPATH,
                            '//*[@id="1"]/section/div[2]/div/div/div[1]/div/div[1]/div/div[2]/span/div').click()
    driverGraf.find_element(By.CLASS_NAME, "css-yn255a-input-input").send_keys(return_reference())
    # driverGraf.find_element(By.CLASS_NAME, "css-yn255a-input-input").send_keys("650cd4fa6e1d3683")  # test
    driverGraf.find_elements(By.CLASS_NAME, "css-yu4292-filterListRow")[0].click()
    driverGraf.find_element(By.XPATH,
                            "/html/body/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]").click()


def filter_by_session():
    session_id = driverGraf.find_element(By.CLASS_NAME, 'css-1w5pd0q')
    # 12
    driverGraf.find_element(By.CLASS_NAME, "css-5t1gy9").click()

    driverGraf.find_element(By.CLASS_NAME, "gf-form-input").send_keys(session_id.text, Keys.RETURN)


def return_session_start_time():
    session_start_time = driverGraf.find_elements(By.CLASS_NAME, "css-1w5pd0q")[5]
    # print("session start time: ", session_start_time.text, "\n")
    return "session start time", session_start_time


def return_session_duration():
    session_duration = driverGraf.find_elements(By.CLASS_NAME, "css-1w5pd0q")[6]
    # print("session duration", session_duration.text, "\n")
    return "session duration", session_duration.text, "\n"


def return_start_latency():
    start_latency = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[5]/div/section/div[2]/div/div[1]").text
    # print(start_latency, "\n")
    return start_latency


def return_playback_start_time():
    playback_start_time = driverGraf.find_element(By.XPATH,
                                                  "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[8]/div/section/div[2]/div/div[1]").text
    # print(playback_start_time, "\n")
    return playback_start_time


def return_final_latency():
    final_latency = driverGraf.find_element(By.XPATH,
                                            "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[5]/div/section/div[2]/div/div[2]").text
    # print(final_latency, "\n")
    return final_latency


def change_chanel():
    secondChanel = qarvaDriver.find_element(By.CLASS_NAME, "Demo_Connected_Channel")
    secondChanel.click()


def return_bitrate_switch_count():
    bitrate_switch_count = driverGraf.find_element(By.XPATH,
                                                   "/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[7]/div/section/div[2]/div/div[1]").text
    # print(bitrate_switch_count, "\n")
    return bitrate_switch_count


def return_interruptions():
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

###############################################
