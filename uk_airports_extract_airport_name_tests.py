"""Tests for extract_airport_name from uk_airports.py."""

from uk_airports import extract_airport_name


def test_extract_airport_name_returns_name():
    airport = {"airport_name": "London Heathrow Airport"}
    assert extract_airport_name(airport) == "London Heathrow Airport"


def test_extract_airport_name_missing_key_returns_empty_string():
    airport = {}
    assert extract_airport_name(airport) == ""


def test_extract_airport_name_ignores_other_keys():
    airport = {"airport_name": "Gatwick", "iata_code": "LGW", "country": "GB"}
    assert extract_airport_name(airport) == "Gatwick"


def test_extract_airport_name_empty_name_string():
    airport = {"airport_name": ""}
    assert extract_airport_name(airport) == ""


def test_extract_airport_name_returns_string():
    airport = {"airport_name": "Stansted"}
    assert isinstance(extract_airport_name(airport), str)


def test_extract_airport_name_name_with_special_characters():
    airport = {"airport_name": "Belfast City (George Best) Airport"}
    assert extract_airport_name(airport) == "Belfast City (George Best) Airport"
