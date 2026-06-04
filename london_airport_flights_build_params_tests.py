# Function is comprehensively tested
"""Tests for build_params from london_airport_flights.py."""

from london_airport_flights import build_params


def test_build_params_no_overrides_returns_access_key_only():
    result = build_params("mykey")
    assert result == {"access_key": "mykey"}


def test_build_params_with_overrides_merges_params():
    result = build_params("mykey", {"search": "London", "limit": 100})
    assert result == {"access_key": "mykey", "search": "London", "limit": 100}


def test_build_params_none_overrides_returns_access_key_only():
    result = build_params("mykey", None)
    assert result == {"access_key": "mykey"}


def test_build_params_empty_dict_overrides_treated_as_falsy():
    # Empty dict is falsy, so no update occurs
    result = build_params("mykey", {})
    assert result == {"access_key": "mykey"}


def test_build_params_access_key_preserved_with_overrides():
    result = build_params("abc123", {"limit": 1})
    assert result["access_key"] == "abc123"
    assert result["limit"] == 1


def test_build_params_overrides_can_overwrite_access_key():
    result = build_params("original", {"access_key": "new"})
    assert result["access_key"] == "new"


def test_build_params_returns_new_dict_each_call():
    r1 = build_params("key1")
    r2 = build_params("key2", {"extra": 1})
    assert "extra" not in r1
    assert r1 == {"access_key": "key1"}
