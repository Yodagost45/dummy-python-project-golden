# Function is comprehensively tested
"""Tests for departure_is_in_window from heathrow_flights.py."""

from heathrow_flights import departure_is_in_window


def _flight(scheduled):
    return {"departure": {"scheduled": scheduled}}


# Happy path: flight time falls strictly inside the window
def test_departure_is_in_window_inside_window():
    assert departure_is_in_window(_flight("2026-06-01T10:30:00"), "10:00", "11:00") is True


# Window is [start, end) — the start minute is included
def test_departure_is_in_window_at_start_inclusive():
    assert departure_is_in_window(_flight("2026-06-01T10:00:00"), "10:00", "11:00") is True


# Window is [start, end) — the end minute is excluded
def test_departure_is_in_window_at_end_exclusive():
    assert departure_is_in_window(_flight("2026-06-01T11:00:00"), "10:00", "11:00") is False


# Flight departs before the window opens
def test_departure_is_in_window_before_window():
    assert departure_is_in_window(_flight("2026-06-01T09:59:00"), "10:00", "11:00") is False


# Flight departs after the window closes
def test_departure_is_in_window_after_window():
    assert departure_is_in_window(_flight("2026-06-01T12:00:00"), "10:00", "11:00") is False


# Empty scheduled string → parse_iso_datetime returns None → False
def test_departure_is_in_window_empty_scheduled_returns_false():
    assert departure_is_in_window({"departure": {"scheduled": ""}}, "10:00", "11:00") is False


# Missing departure key → get_scheduled_departure returns "" → False
def test_departure_is_in_window_missing_departure_returns_false():
    assert departure_is_in_window({}, "10:00", "11:00") is False


# Unparseable datetime string → parse_iso_datetime returns None → False
def test_departure_is_in_window_invalid_scheduled_returns_false():
    assert departure_is_in_window(_flight("not-a-datetime"), "10:00", "11:00") is False


# Timezone-aware strings: hour/minute are read from the local time in the ISO string
def test_departure_is_in_window_with_timezone_offset():
    assert departure_is_in_window(_flight("2026-06-01T10:30:00+01:00"), "10:00", "11:00") is True


# Last minute of the window (10:59) is still inside the [10:00, 11:00) range
def test_departure_is_in_window_last_minute_of_window():
    assert departure_is_in_window(_flight("2026-06-01T10:59:00"), "10:00", "11:00") is True


# Window boundaries work for any hour range, not just the module constants
def test_departure_is_in_window_different_window():
    assert departure_is_in_window(_flight("2026-06-01T14:15:00"), "14:00", "15:00") is True
    assert departure_is_in_window(_flight("2026-06-01T13:59:00"), "14:00", "15:00") is False
