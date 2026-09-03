from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

# Pass options to the driver
driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")


boxes = driver.find_elements(By.CSS_SELECTOR,".form-signin .form-control")
# print(boxes)
for box in boxes:
    # print(box.get_attribute("placeholder"))
    if box.get_attribute("placeholder") == "First Name":
        box.send_keys("Sunny")
    elif box.get_attribute("placeholder") == "Last Name":
        box.send_keys("Dogra")
    else:
        box.send_keys("sunnydogra13@gmail.com")
submit_button = driver.find_element(By.CSS_SELECTOR,".btn-block")
submit_button.send_keys(Keys.ENTER)

