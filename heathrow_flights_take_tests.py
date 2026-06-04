# Function is comprehensively tested
"""Tests for take from heathrow_flights.py."""

from heathrow_flights import take


# Happy path: first n items are returned
def test_take_returns_first_n_items():
    assert take([1, 2, 3, 4, 5], 3) == [1, 2, 3]


# n == len(items) → entire list returned
def test_take_n_equals_length_returns_all():
    assert take([1, 2, 3], 3) == [1, 2, 3]


# n > len(items) → entire list returned without error (slice past end is safe)
def test_take_n_greater_than_length_returns_all():
    assert take([1, 2], 10) == [1, 2]


# n == 0 → empty list (slice [:0])
def test_take_n_zero_returns_empty():
    assert take([1, 2, 3], 0) == []


# Empty input list with any n → empty result
def test_take_empty_list_returns_empty():
    assert take([], 5) == []


# n == 1 → single-element list
def test_take_n_one_returns_single_item():
    assert take(["a", "b", "c"], 1) == ["a"]


# Original insertion order is preserved
def test_take_preserves_order():
    items = [3, 1, 4, 1, 5]
    assert take(items, 4) == [3, 1, 4, 1]


# Works with dict elements (the real use case: flight records)
def test_take_with_dicts():
    flights = [{"id": i} for i in range(5)]
    result = take(flights, 3)
    assert result == [{"id": 0}, {"id": 1}, {"id": 2}]


# Return type is list
def test_take_returns_list():
    assert isinstance(take([1, 2, 3], 2), list)


# The original list is not mutated by the slice operation
def test_take_does_not_mutate_original():
    original = [1, 2, 3, 4]
    take(original, 2)
    assert original == [1, 2, 3, 4]
