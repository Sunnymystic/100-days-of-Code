import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, Mock_API_Endpoint, params):
        self.Mock_API_Endpoint = Mock_API_Endpoint
        self.params = params

    def search_flights(self):
        response = requests.get(self.Mock_API_Endpoint, params=self.params,verify=False)
        print("STATUS CODE:", response.status_code)
        print("URL:", response.url)
        print("CONTENT TYPE:", response.headers.get("Content-Type"))
        print("RESPONSE TEXT:", response.text)
        response.raise_for_status()
        data = response.json()
        return data
        