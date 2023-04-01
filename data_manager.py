import requests
class DataManager:
    """
    This class is responsible for communicating with Google Sheets via Sheety in
    order to collect information on the highest price the user would want to pay
    for each destination.
    """
    def __init__(self, city_codes, city_names, endpoint_edit_data, retrieve_edit_data):
        self.endpoint_retrieve_data = retrieve_edit_data
        self.endpoint_edit_data = endpoint_edit_data
        self.city_codes = city_codes
        self.city_names = city_names
        self.maximum_price = {}

    def add_city_codes(self):
        for code, row in zip(self.city_codes, range(2, len(self.city_codes) + 2)):
            parameters = {
                "price": {
                    "iataCode": code
                }
            }
            requests.put(url=f"{self.endpoint_edit_data}{row}", json=parameters)
        print("City codes added!")

    def retrieve_price_data(self):
        cities = []
        response = requests.get(url=self.endpoint_retrieve_data)
        prices = response.json()
        for i in range(0, len(self.city_names)):
            cities.append({
                "city_name": self.city_names[i],
                "city_code": prices["prices"][i]["iataCode"],
                "price": prices["prices"][i]["lowestPrice"]
            })
        self.maximum_price["Maximum price"] = cities
        return self.maximum_price
