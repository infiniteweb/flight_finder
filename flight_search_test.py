from flight_search import FlightSearch

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_API = "ElS_PdHVv1UHyugKdBeIbDFZa-QJb7ME"
SEARCH_TIME_FRAME = 6
NIGHTS_IN_DESTINATION = 7
CITY_CODES = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]
CITY_NAMES = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York City", "San Francisco",
              "Cape Town"]

flight_search = FlightSearch(flight_endpoint=FLIGHT_ENDPOINT, flight_api=FLIGHT_API,
                             nights_in_destination=NIGHTS_IN_DESTINATION,
                             search_time_frame=SEARCH_TIME_FRAME,  city_codes=CITY_CODES, city_names=CITY_NAMES)

flight_search.search()
