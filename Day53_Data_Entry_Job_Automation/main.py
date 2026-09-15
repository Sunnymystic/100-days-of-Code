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
import requests
from bs4 import BeautifulSoup
import re

sheet_url = "https://docs.google.com/forms/d/e/1FAIpQLSdNFgHmiPZr8ShboWoU4HDX6qh3onI2nsgqNdLY5YmWz6w0eg/viewform?usp=publish-editor"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(zillow_clone_url)
website_html = response.text
addresses = []
links = []
prices = []

soup = BeautifulSoup(website_html,"html.parser")

# links = [
#     link.get("href")
#     for link in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
# ]
# addresses = [
#     address.get_text(strip=True)
#     for address in soup.find_all(name="address", attrs={"data-test": "property-card-link"})
# ]

properties = soup.find_all(
    name="a",
    class_="StyledPropertyCardDataArea-anchor"
)

for property in properties:
    address = property.find("address").get_text(strip=True)
    link = property.get("href")
    # print(f"Address : {address}")
    # print(f"Link : {link}")
    addresses.append(address)
    links.append(link)


print(f"No. of properties links : {len(links)}")
print(f"No. Of addresses : {len(addresses)}")

for i in range(len(addresses)):
    # print(addresses[i])
    result = re.sub(r'[|\s]+', ' ', addresses[i])
    addresses[i] = result

prices_wrappers = soup.find_all(
    name="div",
    class_="PropertyCardWrapper"
)

for price_wrapper in prices_wrappers:
    price = price_wrapper.find("span").get_text(strip=True)
    result = re.split(r'[+/]', price)[0]
    prices.append(result)

# print(prices)

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(sheet_url)
for i in range(len(links)):
    sleep(3)
    input_fields = driver.find_elements(By.CSS_SELECTOR, value=".whsOnd.zHQkBf")
    input_fields[0].send_keys(addresses[i])
    input_fields[1].send_keys(prices[i])
    input_fields[2].send_keys(links[i])
    driver.find_element(By.CSS_SELECTOR, value=".l4V7wb.Fxmcue").click()
    driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a").click()   
    # driver.find_element(By.CSS_SELECTOR, value=".c2gzEf").click()
    # break 
    
    




    