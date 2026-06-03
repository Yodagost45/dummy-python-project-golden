"""Tests for get_airport_name from london_airport_flights.py."""

from london_airport_flights import get_airport_name


def test_get_airport_name_returns_name():
    airport = {"airport_name": "London Heathrow Airport"}
    assert get_airport_name(airport) == "London Heathrow Airport"


def test_get_airport_name_missing_key_returns_empty_string():
    airport = {}
    assert get_airport_name(airport) == ""


def test_get_airport_name_ignores_other_keys():
    airport = {"airport_name": "London City Airport", "iata_code": "LCY", "country": "GB"}
    assert get_airport_name(airport) == "London City Airport"


def test_get_airport_name_empty_name_string():
    airport = {"airport_name": ""}
    assert get_airport_name(airport) == ""


def test_get_airport_name_returns_string():
    airport = {"airport_name": "Gatwick"}
    assert isinstance(get_airport_name(airport), str)


def test_get_airport_name_name_with_parentheses():
    airport = {"airport_name": "Belfast City (George Best) Airport"}
    assert get_airport_name(airport) == "Belfast City (George Best) Airport"
