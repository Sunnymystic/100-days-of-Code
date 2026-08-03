import requests
import smtplib
from datetime import datetime
import time

# MY_LAT = 28.404289
# MY_LONG = 77.290321
MY_LAT = -145.309
MY_LONG = -51.724
def is_iss_overhead(parameters,iss_latitude,iss_longitude):
    if ((iss_latitude-5 <=parameters["lat"] <= iss_latitude + 5) and (iss_longitude - 5 <= parameters["lng"] <= iss_longitude + 5)):
        print("upar hega")
        return True
    else:
        return False
        
def is_night_time():
    if hour >= sunset or hour <= sunrise:
        print("Raat hai")
        return True
    else:
        print("Subha hai")
        return False
     
#Your position is within +5 or -5 degrees of the ISS position.


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude,iss_latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters,verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"sunset : {sunset}")
print(f"sunrise : {sunrise}")

time_now = datetime.now()
hour = time_now.hour

#If the ISS is close to my current position
to_addresses = ["sunnydogra13@gmail.com"]
while True:
    
    if is_iss_overhead(parameters,iss_longitude,iss_latitude) and is_night_time() :
        print("Asi tusi be k pege lassi")
        my_email = "iamdogra007@gmail.com"
        password = "isssyxsnswhaidbn"
        to_address = to_addresses
        with smtplib.SMTP("smtp.gmail.com",587) as connection:  # Build connection
            connection.starttls()                       # Secure connection
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg="Subject:Iss above\n\nLook up to see the ISS"
        )
    time.sleep(10)
        
    
    
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



