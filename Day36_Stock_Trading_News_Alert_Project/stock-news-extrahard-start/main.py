import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests_cache

load_dotenv()
requests_cache.install_cache('stock_price_cache', expire_after=3600)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DECREASE = "🔻"
INCREASE = "🔺"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
RECIPIENT_PHONE = os.getenv("RECIPIENT_PHONE")
percentage = 0.0

def need_to_fetch_news(day1,day2):
    global percentage
    percentage = ((day1-day2)/day1)*100
    # print(percentage)
    print(percentage,day1, day2)
    if percentage >= 0.5:
        return True
    else:
        return False

def fetch_news(change):
    global percentage
    news_array = []
    print("Inside Fetch_news")
    url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWSAPI_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3,
    }
    response = requests.get(url,params=news_params,verify=False)
    response.raise_for_status()
    news_data = response.json()
    # print(news_data)
    if change == "decrease":
        symbol = DECREASE
    else:
        symbol = INCREASE
    news_array = [f"{STOCK}: {symbol}{percentage:.2f}%\nHeadline: {news['title']}\nBrief: {news['description']}" for news in news_data["articles"]]
    for news in news_array:
        print(news)
    return news_array

def send_sms(body: str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=RECIPIENT_PHONE,
        from_=TWILIO_PHONE,
        body=body,
    )
    print(message.body)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## Fetch the end of day data of yesterday's and the day before yesterday


OEM_ENDPOINT = "https://www.alphavantage.co/query"

stocks_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHAVANTAGE_API_KEY,
}

response = requests.get(OEM_ENDPOINT,params=stocks_params,verify=False)
response.raise_for_status()
data = response.json()
source:str = "CACHE" if getattr(response, 'from_cache',False) else 'API'


dates = list(data["Time Series (Daily)"].keys())

last_trading_day_closing_price = float(data["Time Series (Daily)"][dates[0]]["4. close"])
last_to_last_trading_day_closing_price = float(data["Time Series (Daily)"][dates[1]]["4. close"])

if last_trading_day_closing_price >= last_to_last_trading_day_closing_price:
    if need_to_fetch_news(last_trading_day_closing_price,last_to_last_trading_day_closing_price):
        print(source)
        news_array = fetch_news("increase")
        # send_sms()
    else:
        print("No News, as the price is not increased by 5 percent or more.")
else:
    if need_to_fetch_news(last_to_last_trading_day_closing_price,last_trading_day_closing_price):
        print(source)
        news_array = fetch_news("decrease")
        # send_sms()
    else:
        print("No News, as the price is not decreased by 5 percent or more.")

   
        
        


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

