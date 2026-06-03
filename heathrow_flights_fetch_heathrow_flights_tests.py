"""Tests for fetch_heathrow_flights from heathrow_flights.py."""

from unittest.mock import patch

from heathrow_flights import fetch_heathrow_flights


def test_fetch_heathrow_flights_returns_raw_response():
    fake_response = {"data": [{"flight_number": "BA123"}]}

    with patch("heathrow_flights.make_get_request", return_value=fake_response):
        result = fetch_heathrow_flights("mykey", "LHR", "2026-06-01")

    assert result == fake_response


def test_fetch_heathrow_flights_calls_flights_endpoint():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("mykey", "LHR", "2026-06-01")

    url = mock_req.call_args[0][0]
    assert url.endswith("/flights")


def test_fetch_heathrow_flights_includes_dep_iata_in_params():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["dep_iata"] == "LHR"


def test_fetch_heathrow_flights_includes_flight_date_in_params():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["flight_date"] == "2026-06-01"


def test_fetch_heathrow_flights_includes_access_key_in_params():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("secretkey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "secretkey"


def test_fetch_heathrow_flights_sets_limit_100():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("mykey", "LHR", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 100


def test_fetch_heathrow_flights_uses_provided_iata_not_hardcoded():
    with patch("heathrow_flights.make_get_request", return_value={}) as mock_req:
        fetch_heathrow_flights("mykey", "MAN", "2026-06-01")

    params = mock_req.call_args[0][1]
    assert params["dep_iata"] == "MAN"
