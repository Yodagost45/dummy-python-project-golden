"""Tests for multiply_three from math_functions.py."""

import pytest

from math_functions import multiply_three


# --- Happy path / typical inputs ---

def test_multiply_three_basic_positive():
    # 2 * 3 * 4 = 24
    assert multiply_three(2, 3, 4) == 24


def test_multiply_three_all_ones():
    # Multiplicative identity: 1 * 1 * 1 = 1
    assert multiply_three(1, 1, 1) == 1


def test_multiply_three_identity_element():
    # Multiplying any value by 1 twice leaves it unchanged.
    assert multiply_three(7, 1, 1) == 7


# --- Boundary values ---

def test_multiply_three_all_zeros():
    assert multiply_three(0, 0, 0) == 0


def test_multiply_three_with_single_zero():
    # Any factor of zero collapses the entire product to zero.
    assert multiply_three(5, 0, 3) == 0


def test_multiply_three_one_negative():
    # Odd count of negative factors → negative product.
    # (-1) * 5 * 6 = -30
    assert multiply_three(-1, 5, 6) == -30


def test_multiply_three_two_negatives():
    # Even count of negative factors → positive product.
    # (-2) * (-3) * 4 = 24
    assert multiply_three(-2, -3, 4) == 24


def test_multiply_three_all_negatives():
    # Three negatives → negative product.
    # (-2) * (-3) * (-4) = -24
    assert multiply_three(-2, -3, -4) == -24


def test_multiply_three_negative_one_cubed():
    # (-1) * (-1) * (-1) = -1
    assert multiply_three(-1, -1, -1) == -1


# --- Commutativity ---

def test_multiply_three_is_commutative():
    assert multiply_three(2, 3, 4) == multiply_three(4, 3, 2)
    assert multiply_three(2, 3, 4) == multiply_three(3, 4, 2)


# --- Floats ---

def test_multiply_three_floats():
    # 1.5 * 2.0 * 4.0 = 12.0
    assert multiply_three(1.5, 2.0, 4.0) == pytest.approx(12.0)


def test_multiply_three_mixed_int_and_float():
    # 0.5 * 0.5 * 4 = 1.0
    assert multiply_three(0.5, 0.5, 4) == pytest.approx(1.0)


def test_multiply_three_small_floats():
    # 0.1 * 0.2 * 0.3 ≈ 0.006; floating-point mul needs approx.
    assert multiply_three(0.1, 0.2, 0.3) == pytest.approx(0.006)


# --- Large numbers ---

def test_multiply_three_large_integers():
    # Python ints are arbitrary precision; result is exact.
    assert multiply_three(10**6, 10**6, 10**6) == 10**18


# --- Boolean inputs (bool is a subclass of int in Python) ---

def test_multiply_three_true_acts_as_one():
    # True == 1, so True * 5 * 4 = 20.
    assert multiply_three(True, 5, 4) == 20


def test_multiply_three_false_acts_as_zero():
    # False == 0, so False * anything = 0.
    assert multiply_three(False, 5, 4) == 0


# --- Type errors ---

def test_multiply_three_none_raises_type_error():
    with pytest.raises(TypeError):
        multiply_three(None, 1, 2)


def test_multiply_three_two_strings_raises_type_error():
    # str * str is unsupported; mixing two string args raises TypeError.
    with pytest.raises(TypeError):
        multiply_three("a", "b", 1)
