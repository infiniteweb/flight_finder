class FlightData:

    def __init__(self, price_maximum, flight_prices):
        self.price_maximum = price_maximum
        self.flight_prices = flight_prices
        self.flights_to_send = {}

    def print_dictionaries(self):
        print(self.price_maximum)
        print(self.flight_prices)

    def price_compare(self):
        cities = []
        for i in range(0, len(self.price_maximum["Maximum price"])):
            if self.flight_prices["flights"][i]["price"] < \
               self.price_maximum["Maximum price"][i]["price"]:
                departure_date = self.flight_prices["flights"][i]["departure_date"].split("T")[0]
                return_date = self.flight_prices["flights"][i]["return_date"].split("T")[0]
                cities.append({
                    "city_from": self.flight_prices["flights"][i]["city_from"],
                    "fly_from": self.flight_prices["flights"][i]["departure_airport_code"],
                    "city_to": self.flight_prices["flights"][i]["city_to"],
                    "fly_to": self.flight_prices["flights"][i]["return_airport_code"],
                    "departure_date": departure_date,
                    "return_date": return_date,
                    "price": self.flight_prices["flights"][i]["price"],
                    "link": self.flight_prices["flights"][i]["url"]
                })
        self.flights_to_send["flights"] = cities
        return self.flights_to_send

    def print_flights(self):
        print(self.flights_to_send)

