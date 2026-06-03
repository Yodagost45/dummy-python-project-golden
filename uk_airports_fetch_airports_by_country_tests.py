"""Tests for fetch_airports_by_country from uk_airports.py."""

from unittest.mock import patch

from uk_airports import fetch_airports_by_country, BASE_URL


# --- Happy path ---

def test_fetch_airports_by_country_returns_raw_response():
    fake_response = {"data": [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]}

    with patch("uk_airports.make_get_request", return_value=fake_response):
        result = fetch_airports_by_country("mykey", "GB")

    assert result == fake_response


def test_fetch_airports_by_country_returns_empty_data_response():
    fake_response = {"data": []}

    with patch("uk_airports.make_get_request", return_value=fake_response):
        result = fetch_airports_by_country("mykey", "GB")

    assert result == fake_response


# --- URL ---

def test_fetch_airports_by_country_calls_airports_endpoint():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url.endswith("/airports")


def test_fetch_airports_by_country_url_uses_base_url():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url.startswith(BASE_URL)


def test_fetch_airports_by_country_full_url_is_correct():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url == f"{BASE_URL}/airports"


# --- Params: country_iso2 ---

def test_fetch_airports_by_country_includes_country_iso2_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "GB"


def test_fetch_airports_by_country_uses_provided_country_code_not_hardcoded():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "US")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "US"


def test_fetch_airports_by_country_different_country_codes():
    for code in ["DE", "FR", "JP", "AU"]:
        with patch("uk_airports.make_get_request", return_value={}) as mock_req:
            fetch_airports_by_country("mykey", code)

        params = mock_req.call_args[0][1]
        assert params["country_iso2"] == code


def test_fetch_airports_by_country_empty_country_code_passed_through():
    # The function does not validate the country code; empty string is forwarded as-is
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == ""


# --- Params: access_key ---

def test_fetch_airports_by_country_includes_access_key_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "mykey"


def test_fetch_airports_by_country_uses_provided_access_key_not_hardcoded():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("different_secret", "GB")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "different_secret"


# --- Params: limit ---

def test_fetch_airports_by_country_sets_limit_100():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 100


# --- Params: completeness ---

def test_fetch_airports_by_country_params_contain_exactly_three_keys():
    # Expected keys: access_key, country_iso2, limit — no extras
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert set(params.keys()) == {"access_key", "country_iso2", "limit"}


# --- Call count / delegation ---

def test_fetch_airports_by_country_calls_make_get_request_exactly_once():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    assert mock_req.call_count == 1


def test_fetch_airports_by_country_return_value_is_whatever_make_get_request_returns():
    sentinel = {"unexpected_shape": True, "some_key": [1, 2, 3]}

    with patch("uk_airports.make_get_request", return_value=sentinel):
        result = fetch_airports_by_country("mykey", "GB")

    assert result is sentinel
