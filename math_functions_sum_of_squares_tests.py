# WARNING: Function potentially missing test cases
# QA evaluation notes:
#   - All 13 tests pass and all expected values are computed correctly.
#   - Coverage is strong (positives, zeros, negatives, symmetry, floats, large ints, type errors).
#   - Missing case: boolean inputs. In Python, bool is a subclass of int, so
#     sum_of_squares(True, False, True) returns 2 silently. This behaviour is untested and
#     arguably undefined for this function — add a test to lock down expected behaviour.
#   - Minor: test_sum_of_squares_result_is_non_negative uses a weak assertion (>= 0). It only
#     proves the result is non-negative, not that it is correct. Consider also asserting the
#     exact value (140000) for that input.
"""Tests for sum_of_squares from math_functions.py."""

import pytest

from math_functions import sum_of_squares


# --- Happy path / typical inputs (expected values computed by hand) ---

def test_sum_of_squares_basic_positive():
    # Verifies a standard mixed-positive case produces the correct sum of squares.
    # 2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29
    assert sum_of_squares(2, 3, 4) == 29


def test_sum_of_squares_all_ones():
    # Verifies the simplest non-zero case where each squared term is 1.
    # 1 + 1 + 1 = 3
    assert sum_of_squares(1, 1, 1) == 3


# --- Boundary values ---

def test_sum_of_squares_all_zeros():
    # Tests the zero boundary: all-zero input must return 0.
    assert sum_of_squares(0, 0, 0) == 0


def test_sum_of_squares_with_single_zero():
    # Tests that a single zero argument contributes nothing while the others still count.
    # 0 + 25 + 49 = 74
    assert sum_of_squares(0, 5, 7) == 74


# --- Negative numbers: squaring should always yield non-negative contributions ---

def test_sum_of_squares_all_negative():
    # Confirms squaring removes sign: all-negative input matches the all-positive result.
    # (-2)^2 + (-3)^2 + (-4)^2 = 29, same as the positive case
    assert sum_of_squares(-2, -3, -4) == 29


def test_sum_of_squares_mixed_signs():
    # Confirms correct handling of a mix of negative and positive arguments.
    # (-1)^2 + 2^2 + (-3)^2 = 1 + 4 + 9 = 14
    assert sum_of_squares(-1, 2, -3) == 14


def test_sum_of_squares_result_is_non_negative():
    # Property test: the sum of squares of real numbers is never negative.
    # ISSUE: weak assertion — only checks >= 0, not the exact value. The expected result for
    # this input is 140000; asserting that exact value would make the test far stronger.
    assert sum_of_squares(-100, -200, -300) >= 0


# --- Argument ordering should not matter (symmetric in x, y, z) ---

def test_sum_of_squares_is_order_independent():
    # Verifies the operation is symmetric: permuting the arguments yields the same result.
    assert sum_of_squares(1, 2, 3) == sum_of_squares(3, 2, 1)
    assert sum_of_squares(1, 2, 3) == sum_of_squares(2, 3, 1)


# --- Floats (use approximate equality for floating-point) ---

def test_sum_of_squares_floats():
    # Verifies float inputs, using approx to avoid floating-point equality pitfalls.
    # 1.5^2 + 2.5^2 + 3.5^2 = 2.25 + 6.25 + 12.25 = 20.75
    assert sum_of_squares(1.5, 2.5, 3.5) == pytest.approx(20.75)


def test_sum_of_squares_mixed_int_and_float():
    # Verifies mixed int/float arguments are handled and promoted correctly.
    # 2^2 + 0.5^2 + 4^2 = 4 + 0.25 + 16 = 20.25
    assert sum_of_squares(2, 0.5, 4) == pytest.approx(20.25)


# --- Large values ---

def test_sum_of_squares_large_numbers():
    # Verifies behaviour with large magnitudes (relies on Python's arbitrary-precision ints).
    # Python ints are arbitrary precision, so this should be exact.
    n = 10**6
    assert sum_of_squares(n, n, n) == 3 * (10**12)


# --- Type errors: non-numeric input cannot be squared with ** ---

def test_sum_of_squares_string_raises_type_error():
    # Verifies a string argument raises TypeError (str does not support **).
    with pytest.raises(TypeError):
        sum_of_squares("a", 1, 2)


def test_sum_of_squares_none_raises_type_error():
    # Verifies a None argument raises TypeError (NoneType does not support **).
    with pytest.raises(TypeError):
        sum_of_squares(None, 1, 2)


# --- Boolean inputs (flagged as untested in QA notes above) ---

def test_sum_of_squares_boolean_true_acts_as_one():
    # True == 1, False == 0; True^2 + False^2 + True^2 = 1 + 0 + 1 = 2
    assert sum_of_squares(True, False, True) == 2


def test_sum_of_squares_all_false_acts_as_zero():
    # False == 0; 0^2 + 0^2 + 0^2 = 0
    assert sum_of_squares(False, False, False) == 0


# --- Stronger large-number assertion (addresses weak >= 0 check noted above) ---

def test_sum_of_squares_large_negatives_exact_value():
    # (-100)^2 + (-200)^2 + (-300)^2 = 10000 + 40000 + 90000 = 140000
    assert sum_of_squares(-100, -200, -300) == 140000
