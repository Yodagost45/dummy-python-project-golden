"""Tests for filter_by_departure_window from heathrow_flights.py."""

from heathrow_flights import filter_by_departure_window


def _flight(scheduled):
    return {"departure": {"scheduled": scheduled}}


def test_filter_by_departure_window_returns_matching_flights():
    flights = [
        _flight("2026-06-01T09:30:00"),
        _flight("2026-06-01T10:15:00"),
        _flight("2026-06-01T10:45:00"),
        _flight("2026-06-01T11:30:00"),
    ]
    result = filter_by_departure_window(flights, "10:00", "11:00")
    assert len(result) == 2


def test_filter_by_departure_window_empty_list():
    assert filter_by_departure_window([], "10:00", "11:00") == []


def test_filter_by_departure_window_all_in_window():
    flights = [
        _flight("2026-06-01T10:00:00"),
        _flight("2026-06-01T10:30:00"),
        _flight("2026-06-01T10:59:00"),
    ]
    result = filter_by_departure_window(flights, "10:00", "11:00")
    assert len(result) == 3


def test_filter_by_departure_window_none_in_window():
    flights = [
        _flight("2026-06-01T08:00:00"),
        _flight("2026-06-01T12:00:00"),
    ]
    result = filter_by_departure_window(flights, "10:00", "11:00")
    assert result == []


def test_filter_by_departure_window_excludes_end_boundary():
    flights = [
        _flight("2026-06-01T10:00:00"),  # included
        _flight("2026-06-01T11:00:00"),  # excluded (at end)
    ]
    result = filter_by_departure_window(flights, "10:00", "11:00")
    assert len(result) == 1
    assert result[0]["departure"]["scheduled"] == "2026-06-01T10:00:00"


def test_filter_by_departure_window_excludes_invalid_scheduled():
    flights = [
        _flight(""),
        _flight("2026-06-01T10:15:00"),
    ]
    result = filter_by_departure_window(flights, "10:00", "11:00")
    assert len(result) == 1


def test_filter_by_departure_window_preserves_flight_data():
    flight = _flight("2026-06-01T10:30:00")
    result = filter_by_departure_window([flight], "10:00", "11:00")
    assert result[0] is flight


def test_filter_by_departure_window_returns_list():
    result = filter_by_departure_window([], "10:00", "11:00")
    assert isinstance(result, list)
