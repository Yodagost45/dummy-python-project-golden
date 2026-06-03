import requests
from datetime import datetime

API_KEY = "136e0b79e386e7502b0c9059f6b2c20d"
BASE_URL = "http://api.aviationstack.com/v1"
HEATHROW_IATA = "LHR"
FLIGHT_DATE = "2026-06-01"
WINDOW_START = "10:00"
WINDOW_END = "11:00"
RESULT_COUNT = 3


def start():
    raw = fetch_heathrow_flights(API_KEY, HEATHROW_IATA, FLIGHT_DATE)
    flights = extract_flights(raw)
    in_window = filter_by_departure_window(flights, WINDOW_START, WINDOW_END)
    return take(in_window, RESULT_COUNT)


def build_url(endpoint):
    return f"{BASE_URL}/{endpoint}"


def build_params(access_key, overrides=None):
    params = {"access_key": access_key}
    if overrides:
        params.update(overrides)
    return params


def make_get_request(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_heathrow_flights(access_key, dep_iata, flight_date):
    url = build_url("flights")
    params = build_params(access_key, {
        "dep_iata": dep_iata,
        "flight_date": flight_date,
        "limit": 100,
    })
    return make_get_request(url, params)


def extract_flights(response_data):
    return response_data.get("data", [])


def get_scheduled_departure(flight):
    return flight.get("departure", {}).get("scheduled", "")


def parse_iso_datetime(iso_string):
    if not iso_string:
        return None
    try:
        return datetime.fromisoformat(iso_string)
    except ValueError:
        return None


def time_as_tuple(time_string):
    hours, minutes = map(int, time_string.split(":"))
    return (hours, minutes)


def departure_is_in_window(flight, window_start, window_end):
    scheduled_str = get_scheduled_departure(flight)
    dt = parse_iso_datetime(scheduled_str)
    if dt is None:
        return False
    flight_time = (dt.hour, dt.minute)
    return time_as_tuple(window_start) <= flight_time < time_as_tuple(window_end)


def filter_by_departure_window(flights, window_start, window_end):
    return [f for f in flights if departure_is_in_window(f, window_start, window_end)]


def take(items, count):
    return items[:count]
