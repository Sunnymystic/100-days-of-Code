from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_experimental_option("detach", True)

# Pass options to the driver
driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# event = driver.find_element(By.XPATH,value='//*[@id="mwDA"]')
# event = driver.find_element(By.CSS_SELECTOR,"#articlecount a")

# print(event.get_attribute("href"))
# event.click()

all_portals = driver.find_element(By.LINK_TEXT,"Content portals")
all_portals.click()

#Typing in the search bar
search_bar = driver.find_element(By.NAME, value="search")

#sending keyboard input to Selenium
search_bar.send_keys("Python",Keys.ENTER)
# search_bar.send_keys(Keys.ENTER)









# driver.quit()