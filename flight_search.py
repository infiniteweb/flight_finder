import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

'''
To install dateutil run "pip install python-dateutil in the terminal"
'''


class FlightSearch:
    """
    This class communicates with the tequila API to collect data of the selected
    flights.
    """
    def __init__(self, flight_endpoint, flight_api, city_codes, city_names,
                 search_time_frame, nights_in_destination):
        self.flight_api = flight_api
        self.flight_endpoint = flight_endpoint
        self.city_codes = city_codes
        self.city_names = city_names
        self.nights_in_destination = nights_in_destination
        self.now = datetime.now()
        self.date_from = self.now.strftime("%d/%m/%Y")
        self.six_months_from_now = self.now + relativedelta(months=search_time_frame)
        self.date_to = self.six_months_from_now.strftime("%d/%m/%Y")
        self.flight_lowest_price = {}

    def search(self):
        cities = []
        header = {
            "apikey": self.flight_api
        }
        for code in (self.city_codes):
            parameters = {
                "fly_from": "LON",
                "fly_to": code,
                "nights_in_dst_from": self.nights_in_destination,
                "nights_in_dst_to": self.nights_in_destination,
                "one_for_city": 1,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "curr": "GBP"
            }
            response = requests.get(url=self.flight_endpoint, params=parameters, headers=header)
            flights = response.json()
            cities.append({
                "city_from": flights["data"][0]["cityFrom"],
                "city_to": flights["data"][0]["cityTo"],
                "departure_date": flights["data"][0]["route"][0]["local_departure"],
                "return_date": flights["data"][0]["route"][0]["local_departure"],
                "departure_airport_code": flights["data"][0]["flyFrom"],
                "return_airport_code": flights["data"][0]["route"][1]["flyFrom"],
                "city_code": flights["data"][0]["cityCodeTo"],
                "price": flights["data"][0]["price"],
                "url": flights["data"][0]["deep_link"]
            })
        self.flight_lowest_price["flights"] = cities

        return self.flight_lowest_price
