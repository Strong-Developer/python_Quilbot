from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
import time
import pathlib
import speech_recognition as sr
import ffmpy
import requests
import urllib
from pydub import AudioSegment
import os

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(str(pathlib.Path(__file__).parent.absolute()) + '\\chromedriver.exe',options=options)
url="https://quillbot.com/"
driver.get(url)

eleInputbox = driver.find_element_by_id('inputText')

sInput = "The tutorial begins by introducing what bitcoins are, then proceeds with the installation of the bitcoin client software and wallets to make bitcoins transactions possible."

eleInputbox.clear()
eleInputbox.send_keys(sInput)

eleSliders = driver.find_elements_by_class_name('MuiSlider-thumbColorPrimary')

for i in range(0, len(eleSliders)):
    try:
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
    except:
        pass

WebDriverWait(driver, 200).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0'))).click()
time.sleep(1)

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0')))

sOutput = driver.find_element_by_id('articleTextArea').text

time.sleep(1)









