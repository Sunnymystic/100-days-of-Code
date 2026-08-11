#This file will need to use the DataManager,FlightSearch, FlightData, 
# NotificationManager classes to achieve the program requirements.

#requests -- for making API calls

#requests_cache -- for caching API responses locally so you don't burn through your free tier during development

#python-dotenv -- for loading secrets from a .env file (optional but handy)

#twilio -- for sending SMS/WhatsApp notifications

import os
from dotenv import load_dotenv 
import requests
from datetime import datetime, timedelta
import serpapi
import requests_cache

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData  

load_dotenv()
data_manager = DataManager()
# print(DataManager)
# print(DataManager.__module__)
# print(dir(DataManager))
places_to_go = data_manager.get_places_to_go()
tomorrow = datetime.now() + timedelta(days=1)
six_month_later = tomorrow + timedelta(days=10)
to_date = tomorrow.strftime("%Y-%m-%d")
end_date = six_month_later.strftime("%Y-%m-%d")
search_date = to_date

# print(len(places_to_go["destinations"]))
for destination in places_to_go["destinations"]:
  print(f"Searching for flights from {destination['from']} to {destination['to']} between {to_date} and {end_date}...") 
  while search_date <= end_date:
    params = {
                "engine":        "google_flights",
                "departure_id":  destination["from"],
                "arrival_id":    destination["to"],
                "outbound_date": search_date,
                "type":          "2",
                "adults":        "1",
                "currency":      "GBP",
                "stops":         "1",
                "api_key":       os.getenv("MOCK_APP_KEY"),
            }
    # print(os.getenv("MOCK_APP_KEY"))
    flight_data = FlightData(params)
    flight_data_result = flight_data.get_flight_data()               
    if "error" in flight_data_result:
        print("API error:", flight_data_result.get("error"))
    else:
        flights = flight_data_result.get("best_flights", []) + flight_data_result.get("other_flights", [])
        cheapest_overall = None
        if flights:
          cheapest_for_date = min(flights, key=lambda f: f["price"])
          if (
              cheapest_overall is None
              or cheapest_for_date["price"] < cheapest_overall["price"]
          ): cheapest_overall = cheapest_for_date
    search_date = (datetime.strptime(search_date, "%Y-%m-%d")+ timedelta(days=1)).strftime("%Y-%m-%d")
  if cheapest_overall:
    print(f"Cheapest flight for {destination['to']}: GBP {cheapest_overall['price']}")
  else:
    print("No flights found for destination: ", destination['to'])
      



