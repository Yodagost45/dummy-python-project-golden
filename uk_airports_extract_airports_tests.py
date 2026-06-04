# Function is comprehensively tested
"""Tests for extract_airports from uk_airports.py."""

from uk_airports import extract_airports


# Happy path: "data" list is returned directly
def test_extract_airports_returns_data_list():
    response = {"data": [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]}
    assert extract_airports(response) == [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]


# "data" key present but empty → returns []
def test_extract_airports_empty_data():
    response = {"data": []}
    assert extract_airports(response) == []


# Missing "data" key → default of [] is returned
def test_extract_airports_missing_data_key_returns_empty_list():
    response = {}
    assert extract_airports(response) == []


# Extra top-level keys (e.g. pagination) are ignored
def test_extract_airports_ignores_other_keys():
    response = {"data": [{"airport_name": "Heathrow"}], "pagination": {"total": 1}}
    assert extract_airports(response) == [{"airport_name": "Heathrow"}]


# Single-element list is returned as-is (no unwrapping)
def test_extract_airports_single_airport():
    response = {"data": [{"airport_name": "Stansted", "iata_code": "STN"}]}
    assert extract_airports(response) == [{"airport_name": "Stansted", "iata_code": "STN"}]


# Return type is always list
def test_extract_airports_returns_list_type():
    assert isinstance(extract_airports({"data": []}), list)


# Large lists are returned intact without truncation
def test_extract_airports_many_airports():
    airports = [{"airport_name": f"Airport {i}"} for i in range(50)]
    response = {"data": airports}
    assert extract_airports(response) == airports
