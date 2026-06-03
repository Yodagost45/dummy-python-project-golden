"""Tests for get_flight_iata_number from london_airport_flights.py."""

from london_airport_flights import get_flight_iata_number


def test_get_flight_iata_number_returns_iata():
    flight = {"flight": {"iata": "BA100"}}
    assert get_flight_iata_number(flight) == "BA100"


def test_get_flight_iata_number_missing_flight_key_returns_none():
    # .get("flight", {}) falls back to {}; {}.get("iata", None) → None
    assert get_flight_iata_number({}) is None


def test_get_flight_iata_number_missing_iata_key_returns_none():
    assert get_flight_iata_number({"flight": {}}) is None


def test_get_flight_iata_number_iata_explicitly_none_returns_none():
    assert get_flight_iata_number({"flight": {"iata": None}}) is None


def test_get_flight_iata_number_ignores_other_nested_flight_keys():
    flight = {"flight": {"iata": "EZ200", "number": "200", "icao": "EZY200"}}
    assert get_flight_iata_number(flight) == "EZ200"


def test_get_flight_iata_number_ignores_other_top_level_keys():
    flight = {
        "flight": {"iata": "FR1234"},
        "departure": {"iata": "LHR"},
        "arrival": {"iata": "DUB"},
    }
    assert get_flight_iata_number(flight) == "FR1234"


def test_get_flight_iata_number_returns_string():
    assert isinstance(get_flight_iata_number({"flight": {"iata": "TK001"}}), str)


def test_get_flight_iata_number_empty_string_iata():
    # iata present but empty string — returns "" (falsy but not None)
    assert get_flight_iata_number({"flight": {"iata": ""}}) == ""


def test_get_flight_iata_number_flight_value_none_raises():
    # flight key exists but value is None — None.get() raises AttributeError
    import pytest
    with pytest.raises(AttributeError):
        get_flight_iata_number({"flight": None})
