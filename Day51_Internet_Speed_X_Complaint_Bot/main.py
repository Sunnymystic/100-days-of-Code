from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 100
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEED_TEST_WEBSITE = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self,down,up):
        options = Options()
        options.add_experimental_option("detach", True)
        prefs = {
            "profile.default_content_setting_values.geolocation": 2
        }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(SPEED_TEST_WEBSITE)
        self.down_speed_provided = 0.0
        self.up_speed_provided = 0.0
    
    def get_internet_speed(self):
        sleep(3)
        self.driver.find_element(By.XPATH, value='//button[text()="Continue"]').click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "MuiBox-root.css-ketujc").click()
        sleep(50)
        down_speed = self.driver.find_element(
            By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3'
        )
        up_speed = self.driver.find_element(
            By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3'
        )
        self.down_speed_provided = float(down_speed.text)
        self.up_speed_provided = float(up_speed.text)
        if self.down_speed_provided < PROMISED_DOWN or self.up_speed_provided < PROMISED_UP:
            return True
        else:
            return False
        
    def tweet_at_provider(self):
        message = f"Hey Internet Provider, why is my internet speed {self.down_speed_provided} down/{self.up_speed_provided} up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.get(Y_LOGIN_URL)
        sleep(10)
        email_address_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password")))
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".y-btn-primary.y-login-submit")))  
        email_address_field.send_keys(Y_EMAIL)
        password_field.send_keys(Y_PASSWORD)
        submit_button.click()  
        y_compose = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".x-compose")))
        y_compose.send_keys(message)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID,"post-btn"))).click()         
        
        
        
internet_speedtest_bot = InternetSpeedTwitterBot(PROMISED_DOWN,PROMISED_UP)

# email_address_field = float(WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".y-login-wrap input"))))

# internet_speedtest_bot.tweet_at_provider() 
if internet_speedtest_bot.get_internet_speed():
    internet_speedtest_bot.tweet_at_provider() 
    
    
    
    


    