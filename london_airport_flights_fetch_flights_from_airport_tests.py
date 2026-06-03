"""Tests for fetch_flights_from_airport from london_airport_flights.py."""

from unittest.mock import patch

from london_airport_flights import fetch_flights_from_airport


def test_fetch_flights_from_airport_returns_raw_response():
    fake_response = {"data": [{"flight": {"iata": "BA100"}}]}

    with patch("london_airport_flights.make_get_request", return_value=fake_response):
        result = fetch_flights_from_airport("mykey", "LHR", "2026-06-01")

    assert result == fake_response


def test_fetch_flights_from_airport_calls_flights_endpoint():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("mykey", "LHR", "2026-06-01")

    url = mock_req.call_args[0][0]
    assert url.endswith("/flights")


def test_fetch_flights_from_airport_includes_dep_iata_in_params():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["dep_iata"] == "LHR"


def test_fetch_flights_from_airport_includes_flight_date_in_params():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["flight_date"] == "2026-06-01"


def test_fetch_flights_from_airport_includes_access_key_in_params():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("secretkey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "secretkey"


def test_fetch_flights_from_airport_sets_limit_1():
    # Only one flight per airport is needed — limit must be 1
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 1


def test_fetch_flights_from_airport_uses_provided_iata():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_flights_from_airport("mykey", "LCY", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["dep_iata"] == "LCY"
