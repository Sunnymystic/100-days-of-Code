import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import re

password = "isssyxsnswhaidbn"
my_email = "iamdogra007@gmail.com"
to_address = "sunnydogra13@gmail.com"
target_price = 100
price_of_item = 0

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


response = requests.get(url=URL,headers=headers,verify=False)

soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify())

prices = soup.find_all(name="span",id = "apex-pricetopay-accessibility-label",class_="aok-offscreen")

if price_of_item < target_price:
    heading_tag = soup.find_all(name="span",class_="a-size-large product-title-word-break",id="productTitle")
    print(heading_tag)
    # heading = heading_tag[0].text
    # actual_content = heading + "is now available at " + prices[0].getText()
    # clean_title = re.sub(r"\s+", " ", actual_content).strip() + "\n"+ URL
    # print(clean_title)
    
    # msg = EmailMessage()
    # msg["Subject"] = "Amazon Price Alert!"
    # msg["From"] = my_email
    # msg["To"] = to_address

    # msg.set_content(clean_title)

    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.send_message(msg)

    

