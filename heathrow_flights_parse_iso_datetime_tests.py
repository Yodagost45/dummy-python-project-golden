# Function is comprehensively tested
"""Tests for parse_iso_datetime from heathrow_flights.py."""

from datetime import datetime

from heathrow_flights import parse_iso_datetime


# Happy path: a valid ISO string returns a datetime object
def test_parse_iso_datetime_valid_datetime_returns_datetime_object():
    result = parse_iso_datetime("2026-06-01T10:30:00")
    assert isinstance(result, datetime)


# Year, month, and day fields are parsed correctly
def test_parse_iso_datetime_correct_year_month_day():
    result = parse_iso_datetime("2026-06-01T10:30:00")
    assert result.year == 2026
    assert result.month == 6
    assert result.day == 1


# Hour and minute fields are parsed correctly
def test_parse_iso_datetime_correct_hour_and_minute():
    result = parse_iso_datetime("2026-06-01T10:30:00")
    assert result.hour == 10
    assert result.minute == 30


# Timezone-aware strings are accepted; the local time fields are preserved
def test_parse_iso_datetime_with_timezone_offset():
    result = parse_iso_datetime("2026-06-01T10:30:00+01:00")
    assert result is not None
    assert result.hour == 10
    assert result.minute == 30


# Midnight (00:00:00) is parsed correctly — boundary for the day
def test_parse_iso_datetime_midnight():
    result = parse_iso_datetime("2026-06-01T00:00:00")
    assert result is not None
    assert result.hour == 0
    assert result.minute == 0


# End-of-day time is parsed correctly — boundary for the day
def test_parse_iso_datetime_end_of_day():
    result = parse_iso_datetime("2026-06-01T23:59:59")
    assert result is not None
    assert result.hour == 23
    assert result.minute == 59
    assert result.second == 59


# Empty string triggers the `if not iso_string` early-return branch
def test_parse_iso_datetime_empty_string_returns_none():
    assert parse_iso_datetime("") is None


# None triggers the `if not iso_string` early-return branch
def test_parse_iso_datetime_none_returns_none():
    assert parse_iso_datetime(None) is None


# Completely non-date strings are caught by the ValueError handler
def test_parse_iso_datetime_non_date_string_returns_none():
    assert parse_iso_datetime("not-a-date") is None


# Month 13 is out of range — ValueError is caught and None returned
def test_parse_iso_datetime_invalid_month_returns_none():
    assert parse_iso_datetime("2026-13-01T10:00:00") is None


# Hour 99 is out of range — ValueError is caught and None returned
def test_parse_iso_datetime_invalid_hour_returns_none():
    assert parse_iso_datetime("2026-06-01T99:00:00") is None
