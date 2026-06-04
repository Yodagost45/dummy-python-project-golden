# Function is comprehensively tested
"""Tests for fetch_airports_by_country from uk_airports.py."""

from unittest.mock import patch

from uk_airports import fetch_airports_by_country


# Verifies that the raw API response is returned unchanged to the caller
def test_fetch_airports_by_country_returns_raw_response():
    fake_response = {"data": [{"airport_name": "Heathrow"}]}

    with patch("uk_airports.make_get_request", return_value=fake_response):
        result = fetch_airports_by_country("mykey", "GB")

    assert result == fake_response


# Verifies the request targets the "airports" endpoint, not flights or another path
def test_fetch_airports_by_country_calls_airports_endpoint():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url.endswith("/airports")


# Verifies country_iso2 from the caller is forwarded as a query param
def test_fetch_airports_by_country_includes_country_iso2_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "GB"


# Verifies the caller's access_key is forwarded, not a hardcoded value
def test_fetch_airports_by_country_includes_access_key_in_params():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("secretkey", "GB")

    params = mock_req.call_args[0][1]
    assert params["access_key"] == "secretkey"


# Verifies result count is capped at 100 per request
def test_fetch_airports_by_country_sets_limit_100():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert params["limit"] == 100


# Verifies the country_iso2 param uses the caller's value, not a hardcoded "GB"
def test_fetch_airports_by_country_uses_provided_country_code():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "US")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == "US"


# An empty data list is returned as-is without modification
def test_fetch_airports_by_country_returns_empty_data_passthrough():
    fake_response = {"data": []}

    with patch("uk_airports.make_get_request", return_value=fake_response):
        result = fetch_airports_by_country("mykey", "GB")

    assert result == {"data": []}


# URL is rooted at BASE_URL, not just any string ending in "/airports"
def test_fetch_airports_by_country_url_starts_with_base_url():
    from uk_airports import BASE_URL

    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    url = mock_req.call_args[0][0]
    assert url.startswith(BASE_URL)


# An empty country code is forwarded without validation — no guard in the function
def test_fetch_airports_by_country_empty_country_code_forwarded():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "")

    params = mock_req.call_args[0][1]
    assert params["country_iso2"] == ""


# Other country codes are forwarded correctly, not just "GB" and "US"
def test_fetch_airports_by_country_other_country_codes():
    for code in ("DE", "FR", "JP"):
        with patch("uk_airports.make_get_request", return_value={}) as mock_req:
            fetch_airports_by_country("mykey", code)
        params = mock_req.call_args[0][1]
        assert params["country_iso2"] == code


# Params dict contains exactly {access_key, country_iso2, limit} — no extra keys
def test_fetch_airports_by_country_exact_param_keys():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    params = mock_req.call_args[0][1]
    assert set(params.keys()) == {"access_key", "country_iso2", "limit"}


# make_get_request is called exactly once per invocation
def test_fetch_airports_by_country_calls_make_get_request_once():
    with patch("uk_airports.make_get_request", return_value={}) as mock_req:
        fetch_airports_by_country("mykey", "GB")

    assert mock_req.call_count == 1


# The return value is the exact object that make_get_request returned (no copy or wrap)
def test_fetch_airports_by_country_returns_exact_object_from_make_get_request():
    sentinel = {"data": [], "_sentinel": True}

    with patch("uk_airports.make_get_request", return_value=sentinel):
        result = fetch_airports_by_country("mykey", "GB")

    assert result is sentinel
