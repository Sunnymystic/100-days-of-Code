import os
import requests
# import requests_cache


class DataManager:
    def __init__(self):
        self.get_sheety_endpoint = os.getenv("GET_SHEETY_ENDPOINT")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("TOKEN"),
        }

    def get_places_to_go(self):
        # requests_cache.install_cache(
        #     "flight_data_cache",
        #     expire_after=3600
        # )

        response = requests.get(
            self.get_sheety_endpoint,
            headers=self.headers,
            verify=False
        )

        response.raise_for_status()

        data = response.json()

        # source: str = (
        #     "CACHE"
        #     if getattr(response, "from_cache", False)
        #     else "API"
        # )

        return data