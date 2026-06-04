# Function is comprehensively tested
"""Tests for make_get_request from uk_airports.py."""

import pytest
from unittest.mock import MagicMock, patch
import requests

from uk_airports import make_get_request


# Happy path: successful response returns parsed JSON body
def test_make_get_request_returns_json_on_success():
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": []}
    mock_response.raise_for_status.return_value = None

    with patch("uk_airports.requests.get", return_value=mock_response):
        result = make_get_request("http://example.com", {"key": "val"})

    assert result == {"data": []}


# Confirms URL and params are forwarded verbatim to requests.get
def test_make_get_request_calls_get_with_correct_url_and_params():
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    params = {"access_key": "abc", "country_iso2": "GB"}

    with patch("uk_airports.requests.get", return_value=mock_response) as mock_get:
        make_get_request("http://api.example.com/airports", params)

    mock_get.assert_called_once_with("http://api.example.com/airports", params=params)


# raise_for_status() must always be called to propagate 4xx/5xx errors
def test_make_get_request_calls_raise_for_status():
    mock_response = MagicMock()
    mock_response.json.return_value = {}

    with patch("uk_airports.requests.get", return_value=mock_response):
        make_get_request("http://example.com", {})

    mock_response.raise_for_status.assert_called_once()


# A 4xx/5xx status propagates as HTTPError to the caller
def test_make_get_request_raises_http_error_on_bad_status():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("403 Forbidden")

    with patch("uk_airports.requests.get", return_value=mock_response):
        with pytest.raises(requests.exceptions.HTTPError):
            make_get_request("http://example.com", {})


# Network failures propagate without being swallowed
def test_make_get_request_raises_connection_error():
    with patch("uk_airports.requests.get", side_effect=requests.exceptions.ConnectionError()):
        with pytest.raises(requests.exceptions.ConnectionError):
            make_get_request("http://example.com", {})


# Deeply nested JSON payloads are returned intact
def test_make_get_request_returns_nested_json():
    payload = {"data": [{"airport_name": "Heathrow"}], "pagination": {"total": 1}}
    mock_response = MagicMock()
    mock_response.json.return_value = payload
    mock_response.raise_for_status.return_value = None

    with patch("uk_airports.requests.get", return_value=mock_response):
        result = make_get_request("http://example.com", {})

    assert result == payload
