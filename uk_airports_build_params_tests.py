# Function is comprehensively tested
"""Tests for build_params from uk_airports.py."""

from uk_airports import build_params


# No overrides → only access_key in result
def test_build_params_no_overrides_returns_access_key_only():
    result = build_params("mykey")
    assert result == {"access_key": "mykey"}


# Overrides dict is merged into the base params
def test_build_params_with_overrides_merges_params():
    result = build_params("mykey", {"country_iso2": "GB", "limit": 100})
    assert result == {"access_key": "mykey", "country_iso2": "GB", "limit": 100}


# Explicit None overrides behaves the same as no overrides
def test_build_params_none_overrides_returns_access_key_only():
    result = build_params("mykey", None)
    assert result == {"access_key": "mykey"}


# Empty dict is falsy, so no update occurs
def test_build_params_empty_dict_overrides_treated_as_falsy():
    result = build_params("mykey", {})
    assert result == {"access_key": "mykey"}


# access_key survives alongside override keys
def test_build_params_access_key_preserved_with_overrides():
    result = build_params("abc123", {"limit": 100})
    assert result["access_key"] == "abc123"
    assert result["limit"] == 100


# An override can intentionally replace the access_key value
def test_build_params_overrides_can_overwrite_access_key():
    result = build_params("original", {"access_key": "new"})
    assert result["access_key"] == "new"


# Each call returns a fresh dict; state does not accumulate across calls
def test_build_params_returns_new_dict_each_call():
    r1 = build_params("key1")
    r2 = build_params("key2", {"extra": 1})
    assert "extra" not in r1
    assert r1 == {"access_key": "key1"}
