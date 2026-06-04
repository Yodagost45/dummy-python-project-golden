# Function is comprehensively tested
"""Tests for extract_names from uk_airports.py."""

from uk_airports import extract_names


# Happy path: returns a list of name strings in input order
def test_extract_names_returns_list_of_names():
    airports = [
        {"airport_name": "Heathrow"},
        {"airport_name": "Gatwick"},
        {"airport_name": "Stansted"},
    ]
    assert extract_names(airports) == ["Heathrow", "Gatwick", "Stansted"]


# Empty input list → empty output list
def test_extract_names_empty_list_returns_empty_list():
    assert extract_names([]) == []


# Airport dict without airport_name key → extract_airport_name returns ""
def test_extract_names_airport_missing_name_key_returns_empty_string():
    airports = [{"iata_code": "LHR"}]
    assert extract_names(airports) == [""]


# Mixed list: some with names, one missing the key, one with empty string
def test_extract_names_mixed_with_and_without_names():
    airports = [
        {"airport_name": "Heathrow"},
        {"iata_code": "LGW"},  # no airport_name key
        {"airport_name": ""},
    ]
    assert extract_names(airports) == ["Heathrow", "", ""]


# Insertion order is preserved in the output list
def test_extract_names_preserves_order():
    airports = [
        {"airport_name": "C"},
        {"airport_name": "A"},
        {"airport_name": "B"},
    ]
    assert extract_names(airports) == ["C", "A", "B"]


# Return type is list
def test_extract_names_returns_list_type():
    assert isinstance(extract_names([]), list)


# Single-element input → single-element output
def test_extract_names_single_airport():
    airports = [{"airport_name": "Birmingham Airport"}]
    assert extract_names(airports) == ["Birmingham Airport"]
