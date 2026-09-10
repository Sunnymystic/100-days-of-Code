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

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(TINDOG_URL)

try:
    Login_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-tindog-login.tindog-login-pill"))
    )    
    Login_button.click()
    print("Login button found and clicked successfully!")
except NoSuchElementException:
    print("No login button found.")

try:
    facebook_login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-facebark.tindog-login-method"))
    )    
    facebook_login_button.click()
except NoSuchElementException:
    print("No login button found.")

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

try:
    email_address_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "email")
        )
    )
except NoSuchElementException:
    print("email_address field not found.")

try:
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "pass")
        )
    )
except NoSuchElementException:
    print("Password field not found.")

try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/form/button")
        )
    )
except NoSuchElementException:
    print("Submit button not found.")

email_address_field.send_keys(ACCOUNT_EMAIL)
password_field.send_keys(ACCOUNT_PASSWORD)
submit_button.click()
driver.switch_to.window(base_window)
print(driver.title)

# Step 3 — dismiss the three popups
sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Allow"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="Not interested"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="I Accept"]').click()

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)

driver.quit()