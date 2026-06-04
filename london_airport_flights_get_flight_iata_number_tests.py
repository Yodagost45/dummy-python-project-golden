# WARNING: Function potentially missing test cases
# - iata present as empty string "": function returns "" (falsy but not None) — untested;
#   collect_flight_per_airport's `if flight_number:` skips it, but the passthrough is undocumented
# - "flight" key present with value None: None.get() raises AttributeError — untested;
#   this is a real crash scenario if the API returns malformed data
"""Tests for get_flight_iata_number from london_airport_flights.py."""

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
