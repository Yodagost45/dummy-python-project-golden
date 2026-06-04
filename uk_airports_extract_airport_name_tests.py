# Function is comprehensively tested
"""Tests for extract_airport_name from uk_airports.py."""

from uk_airports import extract_airport_name


# Happy path: airport_name value is returned
def test_extract_airport_name_returns_name():
    airport = {"airport_name": "London Heathrow Airport"}
    assert extract_airport_name(airport) == "London Heathrow Airport"


# Missing key → default "" is returned (not None)
def test_extract_airport_name_missing_key_returns_empty_string():
    airport = {}
    assert extract_airport_name(airport) == ""


# Other dict keys do not affect the result
def test_extract_airport_name_ignores_other_keys():
    airport = {"airport_name": "Gatwick", "iata_code": "LGW", "country": "GB"}
    assert extract_airport_name(airport) == "Gatwick"


# Key present with an empty string value is returned as-is
def test_extract_airport_name_empty_name_string():
    airport = {"airport_name": ""}
    assert extract_airport_name(airport) == ""


# Return type is str
def test_extract_airport_name_returns_string():
    airport = {"airport_name": "Stansted"}
    assert isinstance(extract_airport_name(airport), str)


# Names containing parentheses and special characters are preserved verbatim
def test_extract_airport_name_name_with_special_characters():
    airport = {"airport_name": "Belfast City (George Best) Airport"}
    assert extract_airport_name(airport) == "Belfast City (George Best) Airport"
