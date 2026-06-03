"""Tests for fetch_airports_by_country from uk_airports.py."""

from unittest.mock import patch

from uk_airports import fetch_airports_by_country


def test_fetch_airports_by_country_returns_raw_response():
    fake_response = {"data": [{"airport_name": "Heathrow"}]}

    with patch("uk_airports.make_get_request", return_value=fake_response):
        result = fetch_airports_by_country("mykey", "GB")

    assert result == fake_response


def test_fetch_airports_by_country_calls_airports_endpoint():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url.endswith("/airports")


def test_fetch_airports_by_country_includes_country_iso2_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "GB"


def test_fetch_airports_by_country_includes_access_key_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("secretkey", "GB")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "secretkey"


def test_fetch_airports_by_country_sets_limit_100():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 100


def test_fetch_airports_by_country_uses_provided_country_code():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "US")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "US"
