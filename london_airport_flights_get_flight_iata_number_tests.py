# Function is comprehensively tested
"""Tests for get_flight_iata_number from london_airport_flights.py."""

import pytest

from london_airport_flights import get_flight_iata_number


def test_get_flight_iata_number_returns_iata():
    flight = {"flight": {"iata": "BA100"}}
    assert get_flight_iata_number(flight) == "BA100"


def test_get_flight_iata_number_missing_flight_key_returns_none():
    flight = {}
    assert get_flight_iata_number(flight) is None


def test_get_flight_iata_number_missing_iata_key_returns_none():
    flight = {"flight": {}}
    assert get_flight_iata_number(flight) is None


def test_get_flight_iata_number_iata_is_none_returns_none():
    flight = {"flight": {"iata": None}}
    assert get_flight_iata_number(flight) is None


def test_get_flight_iata_number_ignores_other_flight_keys():
    flight = {"flight": {"iata": "EZ200", "number": "200", "icao": "EZY200"}}
    assert get_flight_iata_number(flight) == "EZ200"


def test_get_flight_iata_number_ignores_other_top_level_keys():
    flight = {
        "flight": {"iata": "FR1234"},
        "departure": {"iata": "LHR"},
        "arrival": {"iata": "DUB"},
    }
    assert get_flight_iata_number(flight) == "FR1234"


def test_get_flight_iata_number_returns_string_value():
    flight = {"flight": {"iata": "TK001"}}
    result = get_flight_iata_number(flight)
    assert isinstance(result, str)


# iata is an empty string: returned as "" (falsy, but distinct from None)
def test_get_flight_iata_number_empty_string_iata_returns_empty_string():
    flight = {"flight": {"iata": ""}}
    assert get_flight_iata_number(flight) == ""


# "flight" key present but value is None: chained .get() on None raises AttributeError
def test_get_flight_iata_number_flight_value_is_none_raises_attribute_error():
    flight = {"flight": None}
    with pytest.raises(AttributeError):
        get_flight_iata_number(flight)
