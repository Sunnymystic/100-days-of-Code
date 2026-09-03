from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#You can configure Chrome to stay open even after 
# the script finishes by adding the detach option 
# to your ChromeOptions.
# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Pass options to the driver
driver = webdriver.Chrome(options=options)
# driver.get("https://amazon.in/dp/B09FTCLGMD")
# # a-price-symbol
# # a_price_whole
# # a-price-decimal
# # a-price-fraction

# price_rupees = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"The price is {price_rupees.text}")
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID,value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# print(f"link : {documentation_link.text}")

button_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(button_link.text)

driver.quit()
