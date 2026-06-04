import requests

API_KEY = "136e0b79e386e7502b0c9059f6b2c20d"
BASE_URL = "http://api.aviationstack.com/v1"
UK_COUNTRY_CODE = "GB"


# Function is comprehensively tested
def start():
    raw = fetch_airports_by_country(API_KEY, UK_COUNTRY_CODE)
    airports = extract_airports(raw)
    return extract_names(airports)


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


# WARNING: Function potentially missing test cases - see uk_airports_fetch_airports_by_country_tests.py for details
def fetch_airports_by_country(access_key, country_iso2):
    url = build_url("airports")
    params = build_params(access_key, {
        "country_iso2": country_iso2,
        "limit": 100,
    })
    return make_get_request(url, params)


# Function is comprehensively tested
def extract_airports(response_data):
    return response_data.get("data", [])


# Function is comprehensively tested
def extract_airport_name(airport):
    return airport.get("airport_name", "")


# Function is comprehensively tested
def extract_names(airports):
    return [extract_airport_name(a) for a in airports]
