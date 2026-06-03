"""Tests for extract_airports from uk_airports.py."""

from uk_airports import extract_airports


def test_extract_airports_returns_data_list():
    response = {"data": [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]}
    assert extract_airports(response) == [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]


def test_extract_airports_empty_data():
    response = {"data": []}
    assert extract_airports(response) == []


def test_extract_airports_missing_data_key_returns_empty_list():
    response = {}
    assert extract_airports(response) == []


def test_extract_airports_ignores_other_keys():
    response = {"data": [{"airport_name": "Heathrow"}], "pagination": {"total": 1}}
    assert extract_airports(response) == [{"airport_name": "Heathrow"}]


def test_extract_airports_single_airport():
    response = {"data": [{"airport_name": "Stansted", "iata_code": "STN"}]}
    assert extract_airports(response) == [{"airport_name": "Stansted", "iata_code": "STN"}]


def test_extract_airports_returns_list_type():
    assert isinstance(extract_airports({"data": []}), list)


def test_extract_airports_many_airports():
    airports = [{"airport_name": f"Airport {i}"} for i in range(50)]
    response = {"data": airports}
    assert extract_airports(response) == airports
