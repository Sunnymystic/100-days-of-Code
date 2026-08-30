import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import re


to_address = "sunnydogra13@gmail.com"
# target_price = 100
price_of_item = 0

URL = "https://www.amazon.in/dp/B0GFSW8PDQ"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


response = requests.get(URL, headers=headers)
# print("Status:", response.status_code)
# print("Final URL:", response.url)
# print("Length:", len(response.text))
# print("Title:", BeautifulSoup(response.text, "html.parser").title)
# print("Price ID:", "apex-pricetopay-accessibility-label" in response.text)

with open("amazon_response.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())
print("apex-pricetopay-accessibility-label" in str(soup))
# prices = soup.find_all(name="span",id = "apex-pricetopay-accessibility-label",class_="aok-offscreen")
prices = soup.find_all(name="span",id="apex-pricetopay-accessibility-label",class_="aok-offscreen")

if price_of_item < target_price:
    heading_tag = soup.find_all(name="span",class_="a-size-large product-title-word-break",id="productTitle")
    print(heading_tag)
    print(prices)
    heading = heading_tag[0].text
    actual_content = heading + "is now available at " + prices[0].getText()
    clean_title = re.sub(r"\s+", " ", actual_content).strip() + "\n"+ URL
    print(clean_title)
    
    msg = EmailMessage()
    msg["Subject"] = "Amazon Price Alert!"
    msg["From"] = my_email
    msg["To"] = to_address

    msg.set_content(clean_title)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)

    

