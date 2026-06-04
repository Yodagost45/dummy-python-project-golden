# Function is comprehensively tested
"""Tests for time_as_tuple from heathrow_flights.py."""

import pytest

from heathrow_flights import time_as_tuple


# Happy path: a standard HH:MM string is split and converted
def test_time_as_tuple_standard_time():
    assert time_as_tuple("10:00") == (10, 0)


# Midnight is the lower boundary for hour (0)
def test_time_as_tuple_midnight():
    assert time_as_tuple("00:00") == (0, 0)


# 23:59 is the upper boundary of a valid day time
def test_time_as_tuple_end_of_day():
    assert time_as_tuple("23:59") == (23, 59)


# Non-zero minutes are parsed correctly
def test_time_as_tuple_with_nonzero_minutes():
    assert time_as_tuple("14:30") == (14, 30)


# Leading-zero padding on hour is stripped by int()
def test_time_as_tuple_single_digit_hour_padded():
    assert time_as_tuple("09:05") == (9, 5)


# Both elements are ints, not strings
def test_time_as_tuple_returns_ints_not_strings():
    h, m = time_as_tuple("10:30")
    assert isinstance(h, int)
    assert isinstance(m, int)


# Result is a 2-tuple (hours, minutes)
def test_time_as_tuple_returns_tuple_of_two():
    result = time_as_tuple("11:00")
    assert len(result) == 2


# Input without a colon cannot be unpacked into two variables — raises ValueError
def test_time_as_tuple_no_colon_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("1000")


# Non-numeric hour/minute segments raise ValueError via int()
def test_time_as_tuple_non_numeric_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("ab:cd")


# Empty string produces a single-element split; unpacking to two vars raises ValueError
def test_time_as_tuple_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("")


# First element is hour, second is minute — order matters for comparisons
def test_time_as_tuple_hour_minute_ordering():
    h, m = time_as_tuple("13:45")
    assert h == 13
    assert m == 45
