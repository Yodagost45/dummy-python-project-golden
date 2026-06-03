"""Tests for collect_flight_per_airport from london_airport_flights.py."""

from unittest.mock import patch

from london_airport_flights import collect_flight_per_airport


def _airport(name, iata):
    return {"airport_name": name, "iata_code": iata}


def test_collect_flight_per_airport_returns_name_to_flight_number_dict():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {"Heathrow": "BA100"}


def test_collect_flight_per_airport_skips_airports_with_empty_iata():
    airports = [
        {"airport_name": "Unknown", "iata_code": ""},
        _airport("Heathrow", "LHR"),
    ]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "Unknown" not in result
    assert result == {"Heathrow": "BA100"}


def test_collect_flight_per_airport_skips_airports_with_missing_iata_key():
    airports = [
        {"airport_name": "No IATA"},
        _airport("Gatwick", "LGW"),
    ]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="EZ500"):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "No IATA" not in result
    assert result == {"Gatwick": "EZ500"}


def test_collect_flight_per_airport_skips_when_flight_number_is_none():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value=None):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {}


def test_collect_flight_per_airport_skips_when_flight_number_is_empty_string():
    # get_flight_number_for_airport can return "" when iata exists but is blank.
    # `if flight_number:` is falsy for "", so the airport is correctly excluded.
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value=""):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {}


def test_collect_flight_per_airport_empty_airports_list():
    result = collect_flight_per_airport("mykey", [], "2026-06-01")
    assert result == {}


def test_collect_flight_per_airport_multiple_airports():
    airports = [
        _airport("Heathrow", "LHR"),
        _airport("Gatwick", "LGW"),
        _airport("Stansted", "STN"),
    ]

    def side_effect(key, iata, date):
        return {"LHR": "BA100", "LGW": "EZ200", "STN": "FR300"}[iata]

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=side_effect):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert result == {"Heathrow": "BA100", "Gatwick": "EZ200", "Stansted": "FR300"}


def test_collect_flight_per_airport_calls_get_flight_number_with_correct_args():
    airports = [_airport("Heathrow", "LHR")]

    with patch("london_airport_flights.get_flight_number_for_airport", return_value="BA100") as mock_fn:
        collect_flight_per_airport("secretkey", airports, "2026-06-01")

    mock_fn.assert_called_once_with("secretkey", "LHR", "2026-06-01")


def test_collect_flight_per_airport_mixed_valid_and_no_flight():
    airports = [_airport("Heathrow", "LHR"), _airport("Gatwick", "LGW")]

    def side_effect(key, iata, date):
        return "BA100" if iata == "LHR" else None

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=side_effect):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    assert "Heathrow" in result
    assert "Gatwick" not in result


def test_collect_flight_per_airport_duplicate_airport_name_last_write_wins():
    # Two airports share the same name but have different IATA codes.
    # The second one overwrites the first in the result dict.
    airports = [
        _airport("London Airport", "LHR"),
        _airport("London Airport", "LCY"),
    ]

    def side_effect(key, iata, date):
        return {"LHR": "BA100", "LCY": "BA200"}[iata]

    with patch("london_airport_flights.get_flight_number_for_airport", side_effect=side_effect):
        result = collect_flight_per_airport("mykey", airports, "2026-06-01")

    # Only one entry for the shared name; the second overwrites the first
    assert result["London Airport"] == "BA200"


def test_collect_flight_per_airport_returns_dict_type():
    result = collect_flight_per_airport("mykey", [], "2026-06-01")
    assert isinstance(result, dict)
