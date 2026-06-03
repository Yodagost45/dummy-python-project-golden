"""Tests for get_airport_iata from london_airport_flights.py."""

from london_airport_flights import get_airport_iata


def test_get_airport_iata_returns_iata_code():
    assert get_airport_iata({"iata_code": "LHR"}) == "LHR"


def test_get_airport_iata_missing_key_returns_empty_string():
    assert get_airport_iata({}) == ""


def test_get_airport_iata_empty_iata_code():
    assert get_airport_iata({"iata_code": ""}) == ""


def test_get_airport_iata_ignores_other_keys():
    airport = {"iata_code": "LGW", "airport_name": "Gatwick", "country": "GB"}
    assert get_airport_iata(airport) == "LGW"


def test_get_airport_iata_three_letter_code():
    assert get_airport_iata({"iata_code": "STN"}) == "STN"


def test_get_airport_iata_returns_string_for_valid_key():
    assert isinstance(get_airport_iata({"iata_code": "LCY"}), str)


def test_get_airport_iata_none_value_returns_none():
    # Key present with value None: .get("iata_code", "") returns None (not "")
    # because the default only applies when the key is absent.
    # Callers using `if not iata` will still skip this airport correctly (None is falsy),
    # but the return type differs from the missing-key case — a subtle ambiguity.
    result = get_airport_iata({"iata_code": None})
    assert result is None
