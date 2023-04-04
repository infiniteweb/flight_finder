from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import Notification
import os

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_API = os.environ.get("FLIGHT_API")
SEARCH_TIME_FRAME = 6
NIGHTS_IN_DESTINATION = 7
CITY_NAMES = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York City", "San Francisco",
              "Cape Town"]

SHEET_EDIT_ENDPOINT = "https://api.sheety.co/f3e064d4a97762dab96e2283bfbbe1be/flightDeals/prices/"
SHEET_RETRIEVE_ENDPOINT = "https://api.sheety.co/f3e064d4a97762dab96e2283bfbbe1be/flightDeals/prices"
CITY_CODES = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]

PHONE_NUMBER = "+447888872391"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
recipient_list = os.environ.get("PHONE_NUMBER")

"""
Edit a pre-existing google sheet to add the city codes and then retrieve the maximum
price that the user is willing to pay for a flight.
"""

google_sheet = DataManager(city_codes=CITY_CODES, city_names=CITY_NAMES, endpoint_edit_data=SHEET_EDIT_ENDPOINT,
                           retrieve_edit_data=SHEET_RETRIEVE_ENDPOINT)
# google_sheet.add_city_codes()
price_maximum = google_sheet.retrieve_price_data()

"""
initiate a new flight_search instance and then run a search to return the relevant
flight information.
"""

flight_search = FlightSearch(flight_endpoint=FLIGHT_ENDPOINT, flight_api=FLIGHT_API, city_codes=CITY_CODES,
                             city_names=CITY_NAMES, search_time_frame=SEARCH_TIME_FRAME,
                             nights_in_destination=NIGHTS_IN_DESTINATION)
flight_prices = flight_search.search()


"""
Initiate a new flight data variable to manage the data and to determine if any of 
the pre-requisite prices for locations have been beaten to then move on to the next
step of sending out the notification.
"""

flight_data = FlightData(price_maximum=price_maximum, flight_prices=flight_prices)
flight_data.print_dictionaries()
flight_data.price_compare()
flight_data.print_flights()

"""
check the flight data to see if a notification needs to be sent out and if so send it.
"""

if flight_data.flights_to_send:
    notification = Notification(account_sid=account_sid, auth_token=auth_token,
                                phone_number=PHONE_NUMBER, recipient_list=recipient_list,
                                flights=flight_data.flights_to_send)
    notification.write_text()
    notification.send_text()

