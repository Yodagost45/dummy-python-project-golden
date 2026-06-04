# WARNING: Function potentially missing test cases
# - get_flight_iata_number can return "" (empty string); the function passes it through
#   unchanged — no test documents this, or that collect_flight_per_airport handles it correctly
"""Tests for get_flight_number_for_airport from london_airport_flights.py."""

from unittest.mock import patch

from london_airport_flights import get_flight_number_for_airport


def test_get_flight_number_for_airport_returns_iata_number():
    fake_raw = {"data": [{"flight": {"iata": "BA100"}}]}
    fake_flight = {"flight": {"iata": "BA100"}}

    with patch("london_airport_flights.fetch_flights_from_airport", return_value=fake_raw), \
         patch("london_airport_flights.extract_first_flight", return_value=fake_flight), \
         patch("london_airport_flights.get_flight_iata_number", return_value="BA100"):
        result = get_flight_number_for_airport("mykey", "LHR", "2026-06-01")

    assert result == "BA100"


def test_get_flight_number_for_airport_returns_none_when_no_flights():
    with patch("london_airport_flights.fetch_flights_from_airport", return_value={"data": []}), \
         patch("london_airport_flights.extract_first_flight", return_value=None):
        result = get_flight_number_for_airport("mykey", "LHR", "2026-06-01")

    assert result is None


def test_get_flight_number_for_airport_calls_fetch_with_correct_args():
    with patch("london_airport_flights.fetch_flights_from_airport", return_value={}) as mock_fetch, \
         patch("london_airport_flights.extract_first_flight", return_value=None):
        get_flight_number_for_airport("secretkey", "LCY", "2026-06-01")

    mock_fetch.assert_called_once_with("secretkey", "LCY", "2026-06-01")


def test_get_flight_number_for_airport_passes_raw_to_extract():
    fake_raw = {"data": []}

    with patch("london_airport_flights.fetch_flights_from_airport", return_value=fake_raw), \
         patch("london_airport_flights.extract_first_flight", return_value=None) as mock_extract:
        get_flight_number_for_airport("mykey", "LHR", "2026-06-01")

    mock_extract.assert_called_once_with(fake_raw)


def test_get_flight_number_for_airport_passes_flight_to_get_iata():
    fake_flight = {"flight": {"iata": "EZ500"}}

    with patch("london_airport_flights.fetch_flights_from_airport", return_value={}), \
         patch("london_airport_flights.extract_first_flight", return_value=fake_flight), \
         patch("london_airport_flights.get_flight_iata_number", return_value="EZ500") as mock_iata:
        get_flight_number_for_airport("mykey", "LGW", "2026-06-01")

    mock_iata.assert_called_once_with(fake_flight)


def test_get_flight_number_for_airport_returns_none_when_iata_missing():
    fake_flight = {"flight": {}}

    with patch("london_airport_flights.fetch_flights_from_airport", return_value={}), \
         patch("london_airport_flights.extract_first_flight", return_value=fake_flight), \
         patch("london_airport_flights.get_flight_iata_number", return_value=None):
        result = get_flight_number_for_airport("mykey", "LHR", "2026-06-01")

    assert result is None
