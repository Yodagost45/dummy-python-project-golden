"""Tests for subtract_three from math_functions.py."""

import pytest

from math_functions import subtract_three


# --- Happy path / typical inputs ---

def test_subtract_three_basic_positive():
    # 10 - 3 - 2 = 5
    assert subtract_three(10, 3, 2) == 5


def test_subtract_three_all_ones():
    # 1 - 1 - 1 = -1
    assert subtract_three(1, 1, 1) == -1


# --- Boundary values ---

def test_subtract_three_all_zeros():
    assert subtract_three(0, 0, 0) == 0


def test_subtract_three_only_x_nonzero():
    # Subtracting zeros leaves x unchanged.
    assert subtract_three(10, 0, 0) == 10


def test_subtract_three_all_same_value():
    # x - x - x = -x; with x = 5: 5 - 5 - 5 = -5
    assert subtract_three(5, 5, 5) == -5


def test_subtract_three_result_is_zero():
    # 10 - 6 - 4 = 0
    assert subtract_three(10, 6, 4) == 0


# --- Negative numbers ---

def test_subtract_three_all_negatives():
    # (-5) - (-3) - (-2) = -5 + 3 + 2 = 0
    assert subtract_three(-5, -3, -2) == 0


def test_subtract_three_negative_x():
    # (-1) - 2 - 3 = -6
    assert subtract_three(-1, 2, 3) == -6


def test_subtract_three_negative_y_and_z():
    # 5 - (-3) - (-2) = 5 + 3 + 2 = 10
    assert subtract_three(5, -3, -2) == 10


def test_subtract_three_large_negative_result():
    # 1 - 100 - 100 = -199
    assert subtract_three(1, 100, 100) == -199


# --- Order matters: subtract_three is NOT commutative ---

def test_subtract_three_is_not_commutative():
    # subtract_three(1, 2, 3) = -4, but subtract_three(3, 2, 1) = 0
    assert subtract_three(1, 2, 3) != subtract_three(3, 2, 1)


def test_subtract_three_exact_values_show_order_sensitivity():
    assert subtract_three(1, 2, 3) == -4
    assert subtract_three(3, 2, 1) == 0
    assert subtract_three(10, 3, 2) == 5
    assert subtract_three(3, 10, 2) == -9


# --- Floats ---

def test_subtract_three_floats():
    # 10.5 - 3.5 - 2.0 = 5.0
    assert subtract_three(10.5, 3.5, 2.0) == pytest.approx(5.0)


def test_subtract_three_mixed_int_and_float():
    # 7 - 2.5 - 1 = 3.5
    assert subtract_three(7, 2.5, 1) == pytest.approx(3.5)


def test_subtract_three_negative_float_result():
    # 1.0 - 3.5 - 2.5 = -5.0
    assert subtract_three(1.0, 3.5, 2.5) == pytest.approx(-5.0)


# --- Large numbers ---

def test_subtract_three_large_integers():
    # 10^9 - 10^8 - 10^7 = 890,000,000
    assert subtract_three(10**9, 10**8, 10**7) == 890_000_000


# --- Boolean inputs (bool is a subclass of int in Python) ---

def test_subtract_three_booleans():
    # True == 1, False == 0; True - False - True = 1 - 0 - 1 = 0
    assert subtract_three(True, False, True) == 0


# --- Type errors ---

def test_subtract_three_none_raises_type_error():
    with pytest.raises(TypeError):
        subtract_three(None, 1, 2)


def test_subtract_three_string_raises_type_error():
    with pytest.raises(TypeError):
        subtract_three("a", 1, 2)
