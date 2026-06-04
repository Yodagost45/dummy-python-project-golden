# WARNING: Function potentially missing test cases
# Missing coverage after test file was trimmed:
#   - Empty response passthrough: {"data": []} should be returned unchanged
#   - Full URL assertion: only endsWith("/airports") is checked; BASE_URL prefix is untested
#   - Empty country code passthrough: "" is forwarded to the API without validation (no guard)
#   - Multiple country codes: only "GB" and "US" are exercised; spot-check others (DE, FR, etc.)
#   - Params key set: no test asserts exactly {access_key, country_iso2, limit} with no extras
#   - Call count: no test asserts make_get_request is called exactly once
#   - Return value identity: no test asserts result is the exact object make_get_request returns
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
