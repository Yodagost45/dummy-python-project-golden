# Function is comprehensively tested
"""Tests for get_airport_iata from london_airport_flights.py."""

from london_airport_flights import get_airport_iata


def test_get_airport_iata_returns_iata_code():
    airport = {"iata_code": "LHR"}
    assert get_airport_iata(airport) == "LHR"


def test_get_airport_iata_missing_key_returns_empty_string():
    airport = {}
    assert get_airport_iata(airport) == ""


def test_get_airport_iata_ignores_other_keys():
    airport = {"iata_code": "LGW", "airport_name": "Gatwick", "country": "GB"}
    assert get_airport_iata(airport) == "LGW"


def test_get_airport_iata_empty_iata_code():
    airport = {"iata_code": ""}
    assert get_airport_iata(airport) == ""


def test_get_airport_iata_returns_string():
    airport = {"iata_code": "LCY"}
    assert isinstance(get_airport_iata(airport), str)


def test_get_airport_iata_three_letter_code():
    airport = {"iata_code": "STN"}
    assert get_airport_iata(airport) == "STN"


# "iata_code" key present but value is None: .get() returns None (not the default "")
def test_get_airport_iata_none_iata_code_returns_none():
    airport = {"iata_code": None}
    assert get_airport_iata(airport) is None
