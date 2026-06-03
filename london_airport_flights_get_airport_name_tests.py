"""Tests for get_airport_name from london_airport_flights.py."""

from london_airport_flights import get_airport_name


def test_get_airport_name_returns_name():
    assert get_airport_name({"airport_name": "London Heathrow Airport"}) == "London Heathrow Airport"


def test_get_airport_name_missing_key_returns_empty_string():
    assert get_airport_name({}) == ""


def test_get_airport_name_empty_name_string():
    assert get_airport_name({"airport_name": ""}) == ""


def test_get_airport_name_ignores_other_keys():
    airport = {"airport_name": "London City Airport", "iata_code": "LCY", "country": "GB"}
    assert get_airport_name(airport) == "London City Airport"


def test_get_airport_name_returns_string_for_valid_key():
    assert isinstance(get_airport_name({"airport_name": "Gatwick"}), str)


def test_get_airport_name_name_with_parentheses():
    assert get_airport_name({"airport_name": "Belfast City (George Best) Airport"}) == "Belfast City (George Best) Airport"


def test_get_airport_name_none_value_returns_none():
    # Key present with value None: .get("airport_name", "") returns None (not "")
    # because the default only applies when the key is absent.
    # In collect_flight_per_airport this would create a result entry keyed on None.
    result = get_airport_name({"airport_name": None})
    assert result is None
