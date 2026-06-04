import requests

API_KEY = "136e0b79e386e7502b0c9059f6b2c20d"
BASE_URL = "http://api.aviationstack.com/v1"
LONDON_SEARCH = "London"
FLIGHT_DATE = "2026-06-01"


# Function is comprehensively tested
def start():
    raw = fetch_airports_by_search(API_KEY, LONDON_SEARCH)
    airports = extract_airports(raw)
    return collect_flight_per_airport(API_KEY, airports, FLIGHT_DATE)


# Function is comprehensively tested
def build_url(endpoint):
    return f"{BASE_URL}/{endpoint}"


# Function is comprehensively tested
def build_params(access_key, overrides=None):
    params = {"access_key": access_key}
    if overrides:
        params.update(overrides)
    return params


# Function is comprehensively tested
def make_get_request(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


# WARNING: Function potentially missing test cases - see london_airport_flights_fetch_airports_by_search_tests.py for details
def fetch_airports_by_search(access_key, search_term):
    url = build_url("airports")
    params = build_params(access_key, {
        "search": search_term,
        "limit": 100,
    })
    return make_get_request(url, params)


# WARNING: Function potentially missing test cases - see london_airport_flights_extract_airports_tests.py for details
def extract_airports(response_data):
    return response_data.get("data", [])


# WARNING: Function potentially missing test cases - see london_airport_flights_get_airport_iata_tests.py for details
def get_airport_iata(airport):
    return airport.get("iata_code", "")


# WARNING: Function potentially missing test cases - see london_airport_flights_get_airport_name_tests.py for details
def get_airport_name(airport):
    return airport.get("airport_name", "")


# WARNING: Function potentially missing test cases - see london_airport_flights_fetch_flights_from_airport_tests.py for details
def fetch_flights_from_airport(access_key, iata_code, flight_date):
    url = build_url("flights")
    params = build_params(access_key, {
        "dep_iata": iata_code,
        "flight_date": flight_date,
        "limit": 1,
    })
    return make_get_request(url, params)


# WARNING: Function potentially missing test cases - see london_airport_flights_extract_first_flight_tests.py for details
def extract_first_flight(response_data):
    flights = response_data.get("data", [])
    return flights[0] if flights else None


# WARNING: Function potentially missing test cases - see london_airport_flights_get_flight_iata_number_tests.py for details
def get_flight_iata_number(flight):
    return flight.get("flight", {}).get("iata", None)


# WARNING: Function potentially missing test cases - see london_airport_flights_get_flight_number_for_airport_tests.py for details
def get_flight_number_for_airport(access_key, iata_code, flight_date):
    raw = fetch_flights_from_airport(access_key, iata_code, flight_date)
    flight = extract_first_flight(raw)
    if flight is None:
        return None
    return get_flight_iata_number(flight)


# WARNING: Function potentially missing test cases - see london_airport_flights_collect_flight_per_airport_tests.py for details
def collect_flight_per_airport(access_key, airports, flight_date):
    result = {}
    for airport in airports:
        iata = get_airport_iata(airport)
        name = get_airport_name(airport)
        if not iata:
            continue
        flight_number = get_flight_number_for_airport(access_key, iata, flight_date)
        if flight_number:
            result[name] = flight_number
    return result
