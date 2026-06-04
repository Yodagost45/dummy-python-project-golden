# Function is comprehensively tested
"""Tests for average_three from math_functions.py."""

import pytest

from math_functions import average_three


# --- Happy path / typical inputs ---

def test_average_three_basic_positive():
    # (1 + 2 + 3) / 3 = 2.0
    assert average_three(1, 2, 3) == pytest.approx(2.0)


def test_average_three_all_same():
    # Mean of identical values equals that value.
    # (5 + 5 + 5) / 3 = 5.0
    assert average_three(5, 5, 5) == pytest.approx(5.0)


# --- Boundary values ---

def test_average_three_all_zeros():
    assert average_three(0, 0, 0) == pytest.approx(0.0)


def test_average_three_cancels_to_zero():
    # (-1 + 0 + 1) / 3 = 0.0
    assert average_three(-1, 0, 1) == pytest.approx(0.0)


def test_average_three_non_integer_result():
    # (1 + 2 + 4) / 3 = 7/3 ≈ 2.333…; use approx for repeating decimal.
    assert average_three(1, 2, 4) == pytest.approx(7 / 3)


def test_average_three_single_nonzero():
    # (0 + 0 + 6) / 3 = 2.0
    assert average_three(0, 0, 6) == pytest.approx(2.0)


# --- Negative numbers ---

def test_average_three_all_negatives():
    # (-3 + -6 + -9) / 3 = -18 / 3 = -6.0
    assert average_three(-3, -6, -9) == pytest.approx(-6.0)


def test_average_three_mixed_signs():
    # (-4 + 2 + -2) / 3 = -4/3 ≈ -1.333…
    assert average_three(-4, 2, -2) == pytest.approx(-4 / 3)


def test_average_three_negative_non_integer_mean():
    # (-1 + -2 + -3) / 3 = -6 / 3 = -2.0
    assert average_three(-1, -2, -3) == pytest.approx(-2.0)


# --- Return type: Python 3 / always returns float ---

def test_average_three_returns_float_for_integer_inputs():
    # In Python 3, / always returns float even when the result is whole.
    result = average_three(3, 6, 9)
    assert isinstance(result, float)
    assert result == pytest.approx(6.0)


# --- Commutativity ---

def test_average_three_is_commutative():
    assert average_three(1, 2, 3) == pytest.approx(average_three(3, 2, 1))
    assert average_three(1, 2, 3) == pytest.approx(average_three(2, 3, 1))


# --- Floats ---

def test_average_three_float_inputs():
    # (1.5 + 2.5 + 3.5) / 3 = 7.5 / 3 = 2.5
    assert average_three(1.5, 2.5, 3.5) == pytest.approx(2.5)


def test_average_three_mixed_int_and_float():
    # (2 + 0.5 + 4) / 3 = 6.5 / 3 ≈ 2.1666…
    assert average_three(2, 0.5, 4) == pytest.approx(6.5 / 3)


def test_average_three_negative_floats():
    # (-1.5 + -1.5 + -1.5) / 3 = -1.5
    assert average_three(-1.5, -1.5, -1.5) == pytest.approx(-1.5)


# --- Large numbers ---

def test_average_three_large_integers():
    n = 10**9
    # (n + n + n) / 3 = n
    assert average_three(n, n, n) == pytest.approx(float(n))


# --- Boolean inputs (bool is a subclass of int in Python) ---

def test_average_three_booleans():
    # True == 1, False == 0; (True + True + False) / 3 = 2/3 ≈ 0.666…
    assert average_three(True, True, False) == pytest.approx(2 / 3)


def test_average_three_all_false():
    # False == 0; (0 + 0 + 0) / 3 = 0.0
    assert average_three(False, False, False) == pytest.approx(0.0)


# --- Type errors ---

def test_average_three_none_raises_type_error():
    with pytest.raises(TypeError):
        average_three(None, 1, 2)


def test_average_three_string_raises_type_error():
    with pytest.raises(TypeError):
        average_three("a", 1, 2)
