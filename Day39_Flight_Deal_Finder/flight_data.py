import datetime
import os
from flight_search import FlightSearch
 #This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self,params):
        self.x_app_id =  os.getenv("MOCK_APP_ID")
        self.mock_app_key =  os.getenv("MOCK_APP_KEY")
        self.base_url = "https://app.100daysofpython.dev"
        self.Mock_API_Endpoint = f"{self.base_url}/v1/flights/search"
        self.params = params

    def get_flight_data(self):
        flight_search = FlightSearch(self.Mock_API_Endpoint,self.params)
        get_flight_data = flight_search.search_flights()
        # print("STATUS CODE:", get_flight_data.status_code)
        # print("URL:", get_flight_data.url)
        # print("CONTENT TYPE:", get_flight_data.headers.get("Content-Type"))
        # print("RESPONSE TEXT:", get_flight_data.text)
        return get_flight_data