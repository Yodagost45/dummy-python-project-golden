"""Tests for get_scheduled_departure from heathrow_flights.py."""

import pytest

from heathrow_flights import get_scheduled_departure


def test_get_scheduled_departure_returns_scheduled_string():
    flight = {"departure": {"scheduled": "2026-06-01T10:30:00+00:00"}}
    assert get_scheduled_departure(flight) == "2026-06-01T10:30:00+00:00"


def test_get_scheduled_departure_missing_departure_key_returns_empty():
    flight = {}
    assert get_scheduled_departure(flight) == ""


def test_get_scheduled_departure_missing_scheduled_key_returns_empty():
    flight = {"departure": {}}
    assert get_scheduled_departure(flight) == ""


def test_get_scheduled_departure_empty_scheduled_string():
    flight = {"departure": {"scheduled": ""}}
    assert get_scheduled_departure(flight) == ""


def test_get_scheduled_departure_ignores_other_departure_keys():
    flight = {"departure": {"scheduled": "2026-06-01T10:00:00", "estimated": "2026-06-01T10:05:00"}}
    assert get_scheduled_departure(flight) == "2026-06-01T10:00:00"


def test_get_scheduled_departure_ignores_arrival():
    flight = {
        "departure": {"scheduled": "2026-06-01T10:00:00"},
        "arrival": {"scheduled": "2026-06-01T12:00:00"},
    }
    assert get_scheduled_departure(flight) == "2026-06-01T10:00:00"


def test_get_scheduled_departure_none_departure_raises_attribute_error():
    # departure key exists but is None — .get() on None raises AttributeError
    flight = {"departure": None}
    with pytest.raises(AttributeError):
        get_scheduled_departure(flight)
