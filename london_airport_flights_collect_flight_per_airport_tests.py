# Function is comprehensively tested
"""Tests for collect_flight_per_airport from london_airport_flights.py."""

from unittest.mock import patch, call

from london_airport_flights import collect_flight_per_airport


def _airport(name, iata):
    return {"airport_name": name, "iata_code": iata}


def test_collect_flight_per_airport_returns_dict_of_name_to_flight_number():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {"Heathrow": "BA100"}


def test_collect_flight_per_airport_skips_airports_without_iata():
    airports = [
        {"airport_name": "Unknown", "iata_code": ""},
        _airport("Heathrow", "LHR"),
    ]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "Unknown" not in result
    assert result == {"Heathrow": "BA100"}


def test_collect_flight_per_airport_skips_airports_without_iata_key():
    airports = [
        {"airport_name": "No IATA"},
        _airport("Gatwick", "LGW"),
    ]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="EZ500"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "No IATA" not in result
    assert result == {"Gatwick": "EZ500"}


def test_collect_flight_per_airport_skips_when_no_flight_number():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value=None):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {}


def test_collect_flight_per_airport_empty_airports_returns_empty_dict():
    result = collect_flight_per_airport("mykey", [], "2026-06-01")
    assert result == {}


def test_collect_flight_per_airport_multiple_airports():
    airports = [
        _airport("Heathrow", "LHR"),
        _airport("Gatwick", "LGW"),
        _airport("Stansted", "STN"),
    ]

    def mock_flight_number(key, iata, date):
        return {"LHR": "BA100", "LGW": "EZ200", "STN": "FR300"}[iata]

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=mock_flight_number):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {"Heathrow": "BA100", "Gatwick": "EZ200", "Stansted": "FR300"}


def test_collect_flight_per_airport_calls_get_flight_number_with_correct_args():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100") as mock_fn:
        collect_flight_per_airport("secretkey", airports, "2026-06-01")

    mock_fn.assert_called_once_with("secretkey", "LHR", "2026-06-01")


def test_collect_flight_per_airport_mixed_valid_and_no_flight():
    airports = [
        _airport("Heathrow", "LHR"),
        _airport("Gatwick", "LGW"),
    ]

    def mock_fn(key, iata, date):
        return "BA100" if iata == "LHR" else None

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=mock_fn):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "Heathrow" in result
    assert "Gatwick" not in result


# An empty-string flight number is falsy so the airport is skipped (same path as None)
def test_collect_flight_per_airport_skips_when_flight_number_is_empty_string():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value=""):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {}


# When two airports share a name, the second entry silently overwrites the first
def test_collect_flight_per_airport_duplicate_name_second_overwrites_first():
    airports = [
        _airport("Heathrow", "LHR"),
        _airport("Heathrow", "LHR2"),
    ]

    def mock_fn(key, iata, date):
        return "BA100" if iata == "LHR" else "BA200"

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=mock_fn):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {"Heathrow": "BA200"}
