from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_API = "ElS_PdHVv1UHyugKdBeIbDFZa-QJb7ME"
SEARCH_TIME_FRAME = 6
NIGHTS_IN_DESTINATION = 7
CITY_NAMES = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York City", "San Francisco",
              "Cape Town"]

SHEET_EDIT_ENDPOINT = "https://api.sheety.co/f3e064d4a97762dab96e2283bfbbe1be/flightDeals/prices/"
SHEET_RETRIEVE_ENDPOINT = "https://api.sheety.co/f3e064d4a97762dab96e2283bfbbe1be/flightDeals/prices"
CITY_CODES = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]

google_sheet = DataManager(city_codes=CITY_CODES, city_names=CITY_NAMES, endpoint_edit_data=SHEET_EDIT_ENDPOINT,
                           retrieve_edit_data=SHEET_RETRIEVE_ENDPOINT)
# google_sheet.add_city_codes()
price_maximum = google_sheet.retrieve_price_data()
