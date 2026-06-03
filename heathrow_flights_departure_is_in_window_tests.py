"""Tests for departure_is_in_window from heathrow_flights.py."""

from heathrow_flights import departure_is_in_window


def _flight(scheduled):
    return {"departure": {"scheduled": scheduled}}


def test_departure_is_in_window_inside_window():
    assert departure_is_in_window(_flight("2026-06-01T10:30:00"), "10:00", "11:00") is True


def test_departure_is_in_window_at_start_inclusive():
    # Window is [start, end), so 10:00 should be included
    assert departure_is_in_window(_flight("2026-06-01T10:00:00"), "10:00", "11:00") is True


def test_departure_is_in_window_at_end_exclusive():
    # 11:00 is the exclusive upper bound, so should NOT be in window
    assert departure_is_in_window(_flight("2026-06-01T11:00:00"), "10:00", "11:00") is False


def test_departure_is_in_window_before_window():
    assert departure_is_in_window(_flight("2026-06-01T09:59:00"), "10:00", "11:00") is False


def test_departure_is_in_window_after_window():
    assert departure_is_in_window(_flight("2026-06-01T12:00:00"), "10:00", "11:00") is False


def test_departure_is_in_window_empty_scheduled_returns_false():
    assert departure_is_in_window({"departure": {"scheduled": ""}}, "10:00", "11:00") is False


def test_departure_is_in_window_missing_departure_returns_false():
    assert departure_is_in_window({}, "10:00", "11:00") is False


def test_departure_is_in_window_invalid_scheduled_returns_false():
    assert departure_is_in_window(_flight("not-a-datetime"), "10:00", "11:00") is False


def test_departure_is_in_window_with_timezone_offset():
    # Parsed hour is the local time in the ISO string
    assert departure_is_in_window(_flight("2026-06-01T10:30:00+01:00"), "10:00", "11:00") is True


def test_departure_is_in_window_last_minute_of_window():
    assert departure_is_in_window(_flight("2026-06-01T10:59:00"), "10:00", "11:00") is True


def test_departure_is_in_window_different_window():
    assert departure_is_in_window(_flight("2026-06-01T14:15:00"), "14:00", "15:00") is True
    assert departure_is_in_window(_flight("2026-06-01T13:59:00"), "14:00", "15:00") is False
