"""Tests for build_url from heathrow_flights.py."""

from heathrow_flights import build_url, BASE_URL


def test_build_url_flights_endpoint():
    assert build_url("flights") == f"{BASE_URL}/flights"


def test_build_url_airports_endpoint():
    assert build_url("airports") == f"{BASE_URL}/airports"


def test_build_url_empty_endpoint():
    assert build_url("") == f"{BASE_URL}/"


def test_build_url_nested_path():
    assert build_url("v2/flights") == f"{BASE_URL}/v2/flights"


def test_build_url_starts_with_base_url():
    result = build_url("schedules")
    assert result.startswith(BASE_URL)


def test_build_url_correct_separator():
    result = build_url("endpoint")
    assert result == BASE_URL + "/endpoint"


def test_build_url_returns_string():
    assert isinstance(build_url("flights"), str)
