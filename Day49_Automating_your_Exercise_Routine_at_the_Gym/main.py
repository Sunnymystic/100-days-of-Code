from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  

def print_summary(class_booked, waitlists_joined, already_booked_waitlisted,day,time):
    print("--- BOOKING SUMMARY ---")
    print(f"Classes booked: {class_booked}")
    print(f"Waitlists joined: {waitlists_joined}")
    print(f"Already booked/waitlisted: {already_booked_waitlisted}")
    total = class_booked + waitlists_joined + already_booked_waitlisted
    print(f"Total {day_mapping[day]} {time} classes proccessed: {total}")

day_mapping = {"Mon":"Monday",
               "Tue":"Tuesday",
               "Wed":"Wednesday",
               "Thr":"Thursday",
               "Fri":"Friday",
               "Sat":"Saturday",
               "Sun":"Sunday"}

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

options = Options()
options.add_experimental_option("detach", True)
options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)

driver.get("https://appbrewery.github.io/gym/")

#Click the login button
login_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login-button"))
)

print(login_button.get_attribute("id"))
login_button.click()

email_address_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "email-input")
    )
)

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "password-input")
    )
)

submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "submit-button")
    )
)

email_address_field.send_keys(ACCOUNT_EMAIL)
password_field.send_keys(ACCOUNT_PASSWORD)
submit_button.click()

#check if logged in succesfully?
class_schedule_heading = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".Schedule_scheduleTitle__zfZxg"))
)

print(class_schedule_heading.text)

classes = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".Schedule_dayGroup__y79__")
    )
)
print("Found:", len(classes))

for day_class in classes:
    if "wed" in (day_class.get_attribute("id") or "").lower():
        print("Tuesday found.")
        break

classes = day_class.find_elements(
    By.CSS_SELECTOR,
    ".ClassCard_cardActions__tVZBm"
)

print("Found:", len(classes))

for class_ in classes:
    button_tag = class_.find_element(By.TAG_NAME,"button")
    parent_div = class_.find_element(By.XPATH, "./parent::div")
    class_name = parent_div.find_element(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp h3").text
    day_date = day_class.find_element(By.CSS_SELECTOR,".Schedule_dayGroup__y79__ h2").text    
    day,date = day_date.split(",",1)
    time = parent_div.find_element(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp p").text.split(" ",1)[1]
    class_booked = 0
    waitlists_joined = 0
    already_booked_waitlisted = 0
    print(parent_div.get_attribute("class"))
    if "1700" in (button_tag.get_attribute("id") or "").lower():
        print("Book Button found.")
        if button_tag.text == "Book":
            class_.click()
            class_booked += 1
        elif button_tag.text == "Join Waitlist":
            class_.click()
            waitlists_joined += 1
            print(f"✓ Joined waitlist for: {class_name} on {day_date}")
        elif button_tag.text == "Booked":
            already_booked_waitlisted += 1
            print(f"✓ Already {button_tag.text}: {class_name} on {day_date}")
        else:
            print(f"✓ Already {button_tag.text}: {class_name} on {day_date}")
            already_booked_waitlisted += 1
        break
print_summary(class_booked, waitlists_joined, already_booked_waitlisted,day,time)
            
    
    
