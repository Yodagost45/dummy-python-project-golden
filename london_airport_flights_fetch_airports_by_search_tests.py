"""Tests for fetch_airports_by_search from london_airport_flights.py."""

from unittest.mock import patch

from london_airport_flights import fetch_airports_by_search


def test_fetch_airports_by_search_returns_raw_response():
    fake_response = {"data": [{"airport_name": "London Heathrow"}]}

    with patch("london_airport_flights.make_get_request", return_value=fake_response):
        result = fetch_airports_by_search("mykey", "London")

    assert result == fake_response


def test_fetch_airports_by_search_calls_airports_endpoint():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("mykey", "London")

    url = mock_req.call_args[0][0]
    assert url.endswith("/airports")


def test_fetch_airports_by_search_includes_search_term_in_params():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("mykey", "London")

    params = mock_req.call_args[0][1]
    assert params["search"] == "London"


def test_fetch_airports_by_search_includes_access_key_in_params():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("secretkey", "London")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "secretkey"


def test_fetch_airports_by_search_sets_limit_100():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("mykey", "London")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 100


def test_fetch_airports_by_search_uses_provided_search_term():
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("mykey", "Manchester")

    params = mock_req.call_args[0][1]
    assert params["search"] == "Manchester"


def test_fetch_airports_by_search_empty_search_term_passed_through():
    # The function does not validate the search term; empty string is forwarded as-is
    with patch("london_airport_flights.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_search("mykey", "")

    params = mock_req.call_args[0][1]
    assert params["search"] == ""
