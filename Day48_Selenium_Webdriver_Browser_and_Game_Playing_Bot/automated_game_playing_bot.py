from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time

options = Options()
options.add_experimental_option("detach", True)

# Pass options to the driver
driver = webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")

english_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
)
english_button.click()
last_check = time.monotonic()
time.sleep(2)
while True:
    driver.find_element(By.XPATH,'//*[@id="bigCookie"]').click()
    if time.monotonic() -s last_check >= 5:

        # Reset the timer
        last_check = time.monotonic()

        print("Checking right pane...")

        # 3. Perform your right-pane operation
        items = driver.find_elements(
            By.CSS_SELECTOR,".storeSection .product.unlocked.enabled"
        )
        # print(items)
        if items:
            item_to_select_price = 0
            item_to_select = None
            print("Found", len(items), "items")
            #Get the number of cookies
            number_cookies = number_cookies = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0].replace(",", "").strip())
            print(f"number_cookies:{number_cookies}")

            for item in items:
                try:
                    #Find specific price child node matching the individual product element
                    price_element = item.find_element(By.CSS_SELECTOR, ".price")
                    price_text = price_element.text.replace(",", "").strip()
                    price_text = price_text.replace(",", "").strip()
                    item_price_int = int(price_text)
                    print(f"item_price_int :{item_price_int}")
                    print(f"number_cookies:{number_cookies}")
                    if item_price_int <= number_cookies:
                        if item_to_select_price < item_price_int:
                            print("Inside the comparison checks")
                            item_to_select_price = item_price_int
                            item_to_select = item
                except Exception:
                    continue # Skip structural layout anomalies seamlessly

            if item_to_select:
                print(f"Target Price: {item_to_select_price}")
                print(f"Target ID: {item_to_select.get_attribute('id')}")
                
                # FIX: Changed item_to_select.text() to property access .text
                print(f"Target Text Content:\n{item_to_select.text}") 
                
                try:
                    driver.execute_script("arguments[0].click();", item_to_select)
                    print("Purchase Successful!")
                except Exception as e:
                    print(f"Purchase Unsuccessful! {type(e).__name__}: {e}")







