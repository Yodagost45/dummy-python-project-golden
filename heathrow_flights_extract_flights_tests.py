"""Tests for extract_flights from heathrow_flights.py."""

from heathrow_flights import extract_flights


def test_extract_flights_returns_data_list():
    response = {"data": [{"id": 1}, {"id": 2}]}
    assert extract_flights(response) == [{"id": 1}, {"id": 2}]


def test_extract_flights_empty_data():
    response = {"data": []}
    assert extract_flights(response) == []


def test_extract_flights_missing_data_key_returns_empty_list():
    response = {}
    assert extract_flights(response) == []


def test_extract_flights_ignores_other_keys():
    response = {"data": [{"id": 1}], "pagination": {"total": 1}}
    assert extract_flights(response) == [{"id": 1}]


def test_extract_flights_single_flight():
    response = {"data": [{"flight_number": "BA100"}]}
    assert extract_flights(response) == [{"flight_number": "BA100"}]


def test_extract_flights_many_flights():
    flights = [{"id": i} for i in range(100)]
    response = {"data": flights}
    assert extract_flights(response) == flights


def test_extract_flights_returns_list_type():
    assert isinstance(extract_flights({"data": []}), list)
