import pyshorteners
from twilio.rest import Client


class Notification:
    def __init__(self, account_sid, auth_token, phone_number, recipient_list, flights):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.phone_number = phone_number
        self.recipient_list = recipient_list
        self.flights = flights
        self.text_message = "Price alert! "

        """
        "city_from": flights["data"][0]["cityFrom"],
                "city_to": flights["data"][0]["cityTo"],
                "departure_date": flights["data"][0]["route"][0]["local_departure"],
                "return_date": flights["data"][0]["route"][0]["local_departure"],
                "departure_airport_code": flights["data"][0]["flyFrom"],
                "return_airport_code": flights["data"][0]["route"][1]["flyFrom"],
                "city_code": flights["data"][0]["cityCodeTo"],
                "price": flights["data"][0]["price"],
                "url": flights["data"][0]["deep_link"]
                """

    def write_text(self):
        short = pyshorteners.Shortener()
        for i in range(0, len(self.flights["flights"])):
            price = self.flights["flights"][i]["price"]
            city_from = self.flights["flights"][i]["city_from"]
            fly_from = self.flights["flights"][i]["fly_from"]
            city_to = self.flights["flights"][i]["city_to"]
            fly_to = self.flights["flights"][i]["fly_to"]
            departure_date = self.flights["flights"][i]["departure_date"]
            return_date = self.flights["flights"][i]["return_date"]
            link = short.tinyurl.short(self.flights["flights"][i]["link"])

            self.text_message += f"Only GBP {price} to fly from {city_from}-{fly_from} to " \
                                 f"{city_to}-{fly_to} from {departure_date} to {return_date}. Link {link} "

    def send_text(self):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=self.text_message, from_=self.phone_number,
            to=self.recipient_list)
