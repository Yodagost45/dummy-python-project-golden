# Function is comprehensively tested
"""Tests for start from heathrow_flights.py."""

from unittest.mock import patch

from heathrow_flights import start, API_KEY, HEATHROW_IATA, FLIGHT_DATE, WINDOW_START, WINDOW_END, RESULT_COUNT


# Happy path: result of take() is returned to the caller
def test_start_returns_result_of_take():
    fake_raw = {"data": []}
    fake_flights = [{"id": i} for i in range(5)]
    fake_in_window = fake_flights[:4]
    fake_taken = fake_flights[:3]

    with patch("heathrow_flights.fetch_heathrow_flights", return_value=fake_raw), \
         patch("heathrow_flights.extract_flights", return_value=fake_flights), \
         patch("heathrow_flights.filter_by_departure_window", return_value=fake_in_window), \
         patch("heathrow_flights.take", return_value=fake_taken):
        result = start()

    assert result == fake_taken


# fetch_heathrow_flights is called with the module-level API constants
def test_start_calls_fetch_with_module_constants():
    with patch("heathrow_flights.fetch_heathrow_flights", return_value={}) as mock_fetch, \
         patch("heathrow_flights.extract_flights", return_value=[]), \
         patch("heathrow_flights.filter_by_departure_window", return_value=[]), \
         patch("heathrow_flights.take", return_value=[]):
        start()

    mock_fetch.assert_called_once_with(API_KEY, HEATHROW_IATA, FLIGHT_DATE)


# Extracted flights are passed as the first arg to filter_by_departure_window
def test_start_passes_extract_result_to_filter():
    fake_flights = [{"id": 1}, {"id": 2}]

    with patch("heathrow_flights.fetch_heathrow_flights", return_value={}), \
         patch("heathrow_flights.extract_flights", return_value=fake_flights), \
         patch("heathrow_flights.filter_by_departure_window", return_value=[]) as mock_filter, \
         patch("heathrow_flights.take", return_value=[]):
        start()

    mock_filter.assert_called_once_with(fake_flights, WINDOW_START, WINDOW_END)


# Filtered flights and RESULT_COUNT are passed to take()
def test_start_passes_filter_result_to_take():
    fake_in_window = [{"id": i} for i in range(10)]

    with patch("heathrow_flights.fetch_heathrow_flights", return_value={}), \
         patch("heathrow_flights.extract_flights", return_value=[]), \
         patch("heathrow_flights.filter_by_departure_window", return_value=fake_in_window), \
         patch("heathrow_flights.take", return_value=[]) as mock_take:
        start()

    mock_take.assert_called_once_with(fake_in_window, RESULT_COUNT)


# When nothing matches the window, an empty list is returned
def test_start_returns_empty_when_no_flights_in_window():
    with patch("heathrow_flights.fetch_heathrow_flights", return_value={}), \
         patch("heathrow_flights.extract_flights", return_value=[]), \
         patch("heathrow_flights.filter_by_departure_window", return_value=[]), \
         patch("heathrow_flights.take", return_value=[]):
        result = start()

    assert result == []
