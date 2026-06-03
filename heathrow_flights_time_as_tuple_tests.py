"""Tests for time_as_tuple from heathrow_flights.py."""

import pytest

from heathrow_flights import time_as_tuple


def test_time_as_tuple_standard_time():
    assert time_as_tuple("10:00") == (10, 0)


def test_time_as_tuple_midnight():
    assert time_as_tuple("00:00") == (0, 0)


def test_time_as_tuple_end_of_day():
    assert time_as_tuple("23:59") == (23, 59)


def test_time_as_tuple_with_nonzero_minutes():
    assert time_as_tuple("14:30") == (14, 30)


def test_time_as_tuple_single_digit_hour_padded():
    assert time_as_tuple("09:05") == (9, 5)


def test_time_as_tuple_returns_ints_not_strings():
    h, m = time_as_tuple("10:30")
    assert isinstance(h, int)
    assert isinstance(m, int)


def test_time_as_tuple_returns_tuple_of_two():
    result = time_as_tuple("11:00")
    assert len(result) == 2


def test_time_as_tuple_no_colon_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("1000")


def test_time_as_tuple_non_numeric_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("ab:cd")


def test_time_as_tuple_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        time_as_tuple("")


def test_time_as_tuple_hour_minute_ordering():
    h, m = time_as_tuple("13:45")
    assert h == 13
    assert m == 45
