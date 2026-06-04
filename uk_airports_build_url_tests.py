# Function is comprehensively tested
"""Tests for build_url from uk_airports.py."""

from uk_airports import build_url, BASE_URL


# Confirms "airports" endpoint is correctly appended after a slash
def test_build_url_airports_endpoint():
    assert build_url("airports") == f"{BASE_URL}/airports"


# Confirms "flights" endpoint is correctly appended
def test_build_url_flights_endpoint():
    assert build_url("flights") == f"{BASE_URL}/flights"


# Empty endpoint still produces a trailing slash — documents this edge case
def test_build_url_empty_endpoint():
    assert build_url("") == f"{BASE_URL}/"


# Nested path segments are preserved verbatim
def test_build_url_nested_path():
    assert build_url("v2/airports") == f"{BASE_URL}/v2/airports"


# Result always starts with the configured BASE_URL
def test_build_url_starts_with_base_url():
    result = build_url("schedules")
    assert result.startswith(BASE_URL)


# Separator between base and endpoint is exactly one "/"
def test_build_url_correct_separator():
    result = build_url("ep")
    assert result == BASE_URL + "/ep"


# Return type is str
def test_build_url_returns_string():
    assert isinstance(build_url("airports"), str)
