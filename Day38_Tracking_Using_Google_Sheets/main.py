import os
from dotenv import load_dotenv 
import requests
import datetime

load_dotenv()


url = "https://app.100daysofpython.dev"


x_app_id = os.getenv("X_APP_ID")
x_app_key = os.getenv("X_APP_KEY")
token = os.getenv("TOKEN")
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

post_excercise_data = f"{url}/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": f"{x_app_id}",
    "x-app-key": f"{x_app_key}"
}

data = {
    "query":"swam for 1 hour",
    "weight":76,
    "height_cm":176,
    "age":34,
    "gender":"male",
}

data["query"] = input("What exercise did you do? ")

response = requests.post(post_excercise_data, headers=headers, json=data,verify=False)
result = response.json()
print(result)
# print(result["exercises"][0])
# {'tag_id': 63, 'user_input': 'swam for 1 hour', 'nf_calories': 420, ...}

SHEET_ENDPOINT = sheet_endpoint
headers = {
    "Content-Type": "application/json",
    "Authorization": token,
}

body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

response = requests.post(SHEET_ENDPOINT, headers=headers, json=body,verify=False)
response.raise_for_status()

print(response.json())
print(result["exercises"][0]["duration_min"])