# Function is comprehensively tested
"""Tests for start from uk_airports.py."""

from unittest.mock import patch

from uk_airports import start, API_KEY, UK_COUNTRY_CODE


# Happy path: result of extract_names is returned to the caller
def test_start_returns_list_of_names():
    fake_raw = {"data": []}
    fake_airports = [{"airport_name": "Heathrow"}, {"airport_name": "Gatwick"}]
    fake_names = ["Heathrow", "Gatwick"]

    with patch("uk_airports.fetch_airports_by_country", return_value=fake_raw), \
         patch("uk_airports.extract_airports", return_value=fake_airports), \
         patch("uk_airports.extract_names", return_value=fake_names):
        result = start()

    assert result == fake_names


# fetch_airports_by_country is called with the module-level API constants
def test_start_calls_fetch_with_module_constants():
    with patch("uk_airports.fetch_airports_by_country", return_value={}) as mock_fetch, \
         patch("uk_airports.extract_airports", return_value=[]), \
         patch("uk_airports.extract_names", return_value=[]):
        start()

    mock_fetch.assert_called_once_with(API_KEY, UK_COUNTRY_CODE)


# Raw API response is forwarded to extract_airports unchanged
def test_start_passes_raw_response_to_extract_airports():
    fake_raw = {"data": [{"airport_name": "Heathrow"}]}

    with patch("uk_airports.fetch_airports_by_country", return_value=fake_raw), \
         patch("uk_airports.extract_airports", return_value=[]) as mock_extract, \
         patch("uk_airports.extract_names", return_value=[]):
        start()

    mock_extract.assert_called_once_with(fake_raw)


# Airport list from extract_airports is forwarded to extract_names
def test_start_passes_airports_to_extract_names():
    fake_airports = [{"airport_name": "Heathrow"}]

    with patch("uk_airports.fetch_airports_by_country", return_value={}), \
         patch("uk_airports.extract_airports", return_value=fake_airports), \
         patch("uk_airports.extract_names", return_value=[]) as mock_names:
        start()

    mock_names.assert_called_once_with(fake_airports)


# When no airports are found, an empty list is returned
def test_start_returns_empty_when_no_airports():
    with patch("uk_airports.fetch_airports_by_country", return_value={}), \
         patch("uk_airports.extract_airports", return_value=[]), \
         patch("uk_airports.extract_names", return_value=[]):
        result = start()

    assert result == []
