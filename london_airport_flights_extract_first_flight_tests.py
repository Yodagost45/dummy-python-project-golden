"""Tests for extract_first_flight from london_airport_flights.py."""

from london_airport_flights import extract_first_flight


def test_extract_first_flight_returns_first_element():
    response = {"data": [{"flight_number": "BA100"}, {"flight_number": "BA200"}]}
    assert extract_first_flight(response) == {"flight_number": "BA100"}


def test_extract_first_flight_single_flight():
    response = {"data": [{"flight_number": "BA100"}]}
    assert extract_first_flight(response) == {"flight_number": "BA100"}


def test_extract_first_flight_empty_data_returns_none():
    assert extract_first_flight({"data": []}) is None


def test_extract_first_flight_missing_data_key_returns_none():
    # .get("data", []) returns [] when key absent, so result is None
    assert extract_first_flight({}) is None


def test_extract_first_flight_ignores_subsequent_flights():
    flights = [{"id": i} for i in range(5)]
    assert extract_first_flight({"data": flights}) == {"id": 0}


def test_extract_first_flight_returns_dict_not_list():
    response = {"data": [{"flight": {"iata": "BA100"}}]}
    result = extract_first_flight(response)
    assert isinstance(result, dict)


def test_extract_first_flight_data_none_raises():
    # Key present with value None: .get() returns None, then `if flights` is False
    # so the function returns None rather than raising — documents this edge case.
    result = extract_first_flight({"data": None})
    assert result is None
