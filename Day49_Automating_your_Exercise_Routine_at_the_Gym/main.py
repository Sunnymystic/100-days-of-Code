from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  

def print_summary(class_booked, waitlists_joined, already_booked_waitlisted,day_arr,time,message_arr):
    print("--- BOOKING SUMMARY ---")
    print(f"Classes booked: {class_booked}")
    print(f"Waitlists joined: {waitlists_joined}")
    print(f"Already booked/waitlisted: {already_booked_waitlisted}")
    total = class_booked + waitlists_joined + already_booked_waitlisted
    # print(day)
    # print(f"Total {day_mapping[day_arr[0]]} & {day_mapping[day_arr[1]]} {time} classes proccessed: {total}")
    print ("--- DETAILED CLASS LIST ---")
    for i in range(len(message_arr)):
        print(message_arr[i])


def verify_booking():
    mybooking_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,"my-bookings-link"))
    )
    mybooking_button.click()
    print("--- VERIFYING ON MY BOOKINGS PAGE ---")
    confirmed_bookings = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MyBookings_section__oBwNg"))
    )
    confirmed_bookings_arr = confirmed_bookings.find_elements(
            By.CSS_SELECTOR,".MyBookings_bookingCard__VRdrR"
    )
    number_of_confirmed_bookings = len(confirmed_bookings_arr)
    # print(number_of_confirmed_bookings)
    for i in range(number_of_confirmed_bookings):
        confirmed_class = confirmed_bookings_arr[i].find_element(By.TAG_NAME,"h3").text.strip()
        confirmed_classes_time = confirmed_bookings_arr[i].find_element(By.TAG_NAME,"p").text.split("When: ",1)[1]
        day,date,time = confirmed_classes_time.split(",")
        confirmed_booking_list.append((confirmed_class,day.strip(),date.strip(),time.strip()))
    # print(f"Confirmed Booking List : {confirmed_booking_list}")
    for i in range(len(booked_classes_list)):
        # print(f"Confirmed Booking List : {confirmed_booking_list[i]}")
        # print(f"Booked Classes List: {booked_classes_list[i]}")
        if confirmed_booking_list[i] == booked_classes_list[i]:
            print(f"  ✓ Verified successfully: {confirmed_booking_list[i]}")
        else:
            print(f"  ✖ Verified with error: {confirmed_booking_list[i]}")
    print("--- VERIFICATION RESULT ---")
    print(f"Expected: {len(booked_classes_list)}")
    print(f"Found: {len(confirmed_booking_list)}")
    
    if len(booked_classes_list) == len(confirmed_booking_list):
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {len(booked_classes_list) - len(confirmed_booking_list)} bookings")

    

        # get_the_class_details()
    # mybookings = webdriver.

# ACCOUNT_EMAIL = "sunnydogra@test.com"  # The email you registered with
# ACCOUNT_PASSWORD = "qwerty123!@#"      # The password you used during registration
ACCOUNT_EMAIL = "admin@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "admin123"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

button_tag = None
parent_div = None
class_name = ""
day_date = ""
# day_date_arr = []
day = ""
date = ""
time = ""
day_arr = []
date = ""
class_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0
message = ""
message_arr = []
confirmed_booking_list = []
booked_classes_list = []


day_mapping = {"Mon":"Monday",
               "Tue":"Tuesday",
               "Wed":"Wednesday",
               "Thu":"Thursday",
               "Fri":"Friday",
               "Sat":"Saturday",
               "Sun":"Sunday"}

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

options = Options()
options.add_experimental_option("detach", True)
options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)
driver.refresh()
driver.get("https://appbrewery.github.io/gym/")

#Click the login button
login_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login-button"))
)

# print(login_button.get_attribute("id"))
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

# print(class_schedule_heading.text)

classes = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".Schedule_dayGroup__y79__")
    )
)
# print("Found:", len(classes))

for day_class in classes:
    # print(f"{day_class.get_attribute("id")}")
    if "tue" in (day_class.get_attribute("id") or "").lower() or "thu" in (day_class.get_attribute("id") or "").lower():
        # print(f"{day_class.get_attribute("id")}")
        classes_for_the_day = day_class.find_elements(
            By.CSS_SELECTOR,
            ".ClassCard_cardActions__tVZBm"
        )

        # print("Found:", len(classes_for_the_day))

        for class_ in classes_for_the_day:
            button_tag  = class_.find_element(By.TAG_NAME,"button")
            message = "  • "
            # print(button_tag.get_attribute("id"))
            if "1800" in (button_tag.get_attribute("id") or "").lower():
                # print("My dil goes mmmmm")
                parent_div = class_.find_element(By.XPATH, "./parent::div")
                class_name = parent_div.find_element(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp h3").text
                day_date = day_class.find_element(By.CSS_SELECTOR,".Schedule_dayGroup__y79__ h2").text
                day,date = day_date.split(",",1)
                if ")" in date:
                    updated_date = date.split(")",1)[0]
                # print(f"Booked class name: {class_name.strip()}")
                else:
                    updated_date = date
                # print(f"Booked class date: {updated_date.strip()} {date}")
                if "Today (" in day or "Tomorrow (" in day:
                    day = day.split("(",1)[1]
                # print(f"Booked class day: {day.strip()}")
                day_arr.append(day)
                time = parent_div.find_element(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp p").text.split(" ",1)[1]
                # print(time.strip())
                booked_classes_list.append((class_name.strip(),day.strip(),updated_date.strip(),time.strip()))
                # print("Book Button found.")
                if button_tag.text == "Book Class":
                    class_.click()
                    class_booked += 1
                    print(f"✓ Successfully booked: {class_name} on {day_date}")
                    message = message + "[New Booking] "
                elif button_tag.text == "Join Waitlist":
                    class_.click()
                    waitlists_joined += 1
                    print(f"✓ Joined waitlist for: {class_name} on {day_date}")
                    message = message + "[Waitlist Joined] "
                elif button_tag.text == "Booked":
                    already_booked_waitlisted += 1
                    print(f"✓ Already {button_tag.text}: {class_name} on {day_date}")
                    message = message + "[Already Booked/Waitlisted] "
                else:
                    print(f"✓ Already {button_tag.text}: {class_name} on {day_date}")
                    already_booked_waitlisted += 1
                    message = message + "[Already Booked/Waitlisted] "
                message = message + class_name + " " + "on " +  day_date
                message_arr.append(message)
                break
# print(f"Booked Classes List : ", booked_classes_list)
print_summary(class_booked, waitlists_joined, already_booked_waitlisted,day_arr,time,message_arr)
verify_booking()


            
    
    
