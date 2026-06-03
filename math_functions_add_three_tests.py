"""Tests for add_three from math_functions.py."""

import pytest

from math_functions import add_three


# --- Happy path / typical inputs ---

def test_add_three_basic_positive():
    # 2 + 3 + 4 = 9
    assert add_three(2, 3, 4) == 9


def test_add_three_all_ones():
    assert add_three(1, 1, 1) == 3


# --- Boundary values ---

def test_add_three_all_zeros():
    assert add_three(0, 0, 0) == 0


def test_add_three_with_single_zero():
    # A zero addend contributes nothing; the others still count.
    # 0 + 5 + 7 = 12
    assert add_three(0, 5, 7) == 12


def test_add_three_all_negatives():
    # (-2) + (-3) + (-4) = -9
    assert add_three(-2, -3, -4) == -9


def test_add_three_mixed_signs():
    # (-1) + 2 + (-3) = -2
    assert add_three(-1, 2, -3) == -2


def test_add_three_cancels_to_zero():
    # Opposite values sum to zero.
    # (-3) + 0 + 3 = 0
    assert add_three(-3, 0, 3) == 0


def test_add_three_negative_and_positive_same_magnitude():
    # 5 + (-5) + 0 = 0
    assert add_three(5, -5, 0) == 0


# --- Commutativity ---

def test_add_three_is_commutative():
    assert add_three(1, 2, 3) == add_three(3, 2, 1)
    assert add_three(1, 2, 3) == add_three(2, 3, 1)


# --- Floats ---

def test_add_three_floats():
    # 1.5 + 2.5 + 3.5 = 7.5
    assert add_three(1.5, 2.5, 3.5) == pytest.approx(7.5)


def test_add_three_mixed_int_and_float():
    # 2 + 0.5 + 4 = 6.5
    assert add_three(2, 0.5, 4) == pytest.approx(6.5)


def test_add_three_negative_floats():
    # (-1.1) + 2.2 + (-3.3) = -2.2
    assert add_three(-1.1, 2.2, -3.3) == pytest.approx(-2.2)


# --- Large numbers ---

def test_add_three_large_integers():
    n = 10**9
    assert add_three(n, n, n) == 3 * n


# --- Boolean inputs (bool is a subclass of int in Python) ---

def test_add_three_true_acts_as_one():
    # True == 1; True + True + 1 = 3
    assert add_three(True, True, 1) == 3


def test_add_three_false_acts_as_zero():
    # False == 0; False + 5 + 7 = 12
    assert add_three(False, 5, 7) == 12


# --- Type errors ---

def test_add_three_none_raises_type_error():
    with pytest.raises(TypeError):
        add_three(None, 1, 2)


def test_add_three_mixed_string_and_int_raises_type_error():
    # str + int is unsupported.
    with pytest.raises(TypeError):
        add_three("a", 1, 2)
