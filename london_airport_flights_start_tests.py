"""Tests for start from london_airport_flights.py."""

from unittest.mock import patch

from london_airport_flights import start, API_KEY, LONDON_SEARCH, FLIGHT_DATE


def test_start_returns_dict_of_airport_to_flight_number():
    fake_raw = {"data": []}
    fake_airports = [{"airport_name": "Heathrow", "iata_code": "LHR"}]
    fake_result = {"Heathrow": "BA100"}

    with patch("london_airport_flights.fetch_airports_by_search", return_value=fake_raw), \
         patch("london_airport_flights.extract_airports", return_value=fake_airports), \
         patch("london_airport_flights.collect_flight_per_airport", return_value=fake_result):
        result = start()

    assert result == fake_result


def test_start_calls_fetch_with_module_constants():
    with patch("london_airport_flights.fetch_airports_by_search", return_value={}) as mock_fetch, \
         patch("london_airport_flights.extract_airports", return_value=[]), \
         patch("london_airport_flights.collect_flight_per_airport", return_value={}):
        start()

    mock_fetch.assert_called_once_with(API_KEY, LONDON_SEARCH)


def test_start_passes_raw_response_to_extract_airports():
    fake_raw = {"data": [{"airport_name": "Heathrow"}]}

    with patch("london_airport_flights.fetch_airports_by_search", return_value=fake_raw), \
         patch("london_airport_flights.extract_airports", return_value=[]) as mock_extract, \
         patch("london_airport_flights.collect_flight_per_airport", return_value={}):
        start()

    mock_extract.assert_called_once_with(fake_raw)


def test_start_passes_airports_and_constants_to_collect():
    fake_airports = [{"airport_name": "Heathrow", "iata_code": "LHR"}]

    with patch("london_airport_flights.fetch_airports_by_search", return_value={}), \
         patch("london_airport_flights.extract_airports", return_value=fake_airports), \
         patch("london_airport_flights.collect_flight_per_airport", return_value={}) as mock_collect:
        start()

    mock_collect.assert_called_once_with(API_KEY, fake_airports, FLIGHT_DATE)


def test_start_returns_empty_dict_when_no_airports():
    with patch("london_airport_flights.fetch_airports_by_search", return_value={}), \
         patch("london_airport_flights.extract_airports", return_value=[]), \
         patch("london_airport_flights.collect_flight_per_airport", return_value={}):
        result = start()

    assert result == {}
