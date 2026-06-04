# Function is comprehensively tested
"""Tests for extract_first_flight from london_airport_flights.py."""

from london_airport_flights import extract_first_flight


def test_extract_first_flight_returns_first_element():
    response = {"data": [{"flight_number": "BA100"}, {"flight_number": "BA200"}]}
    assert extract_first_flight(response) == {"flight_number": "BA100"}


def test_extract_first_flight_single_flight():
    response = {"data": [{"flight_number": "BA100"}]}
    assert extract_first_flight(response) == {"flight_number": "BA100"}


def test_extract_first_flight_empty_data_returns_none():
    response = {"data": []}
    assert extract_first_flight(response) is None


def test_extract_first_flight_missing_data_key_returns_none():
    response = {}
    assert extract_first_flight(response) is None


def test_extract_first_flight_ignores_subsequent_flights():
    flights = [{"id": i} for i in range(5)]
    response = {"data": flights}
    assert extract_first_flight(response) == {"id": 0}


def test_extract_first_flight_returns_dict():
    response = {"data": [{"flight": {"iata": "BA100"}}]}
    result = extract_first_flight(response)
    assert isinstance(result, dict)


def test_extract_first_flight_none_on_no_data_key():
    # .get() returns [] by default, so [0] is safe — returns None
    assert extract_first_flight({"other": "stuff"}) is None


# "data" key present but value is None: `if None` is falsy so None is returned safely
def test_extract_first_flight_data_is_none_returns_none():
    response = {"data": None}
    assert extract_first_flight(response) is None
