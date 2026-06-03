"""Tests for make_get_request from london_airport_flights.py."""

import pytest
from unittest.mock import MagicMock, patch
import requests

from london_airport_flights import make_get_request


def test_make_get_request_returns_json_on_success():
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": []}
    mock_response.raise_for_status.return_value = None

    with patch("london_airport_flights.requests.get", return_value=mock_response):
        result = make_get_request("http://example.com", {"key": "val"})

    assert result == {"data": []}


def test_make_get_request_calls_get_with_correct_url_and_params():
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    params = {"access_key": "abc", "search": "London"}

    with patch("london_airport_flights.requests.get", return_value=mock_response) as mock_get:
        make_get_request("http://api.example.com/airports", params)

    mock_get.assert_called_once_with("http://api.example.com/airports", params=params)


def test_make_get_request_calls_raise_for_status():
    mock_response = MagicMock()
    mock_response.json.return_value = {}

    with patch("london_airport_flights.requests.get", return_value=mock_response):
        make_get_request("http://example.com", {})

    mock_response.raise_for_status.assert_called_once()


def test_make_get_request_raises_http_error_on_bad_status():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("403 Forbidden")

    with patch("london_airport_flights.requests.get", return_value=mock_response):
        with pytest.raises(requests.exceptions.HTTPError):
            make_get_request("http://example.com", {})


def test_make_get_request_raises_connection_error():
    with patch("london_airport_flights.requests.get", side_effect=requests.exceptions.ConnectionError()):
        with pytest.raises(requests.exceptions.ConnectionError):
            make_get_request("http://example.com", {})


def test_make_get_request_returns_nested_json():
    payload = {"data": [{"flight": {"iata": "BA100"}}], "pagination": {"total": 1}}
    mock_response = MagicMock()
    mock_response.json.return_value = payload
    mock_response.raise_for_status.return_value = None

    with patch("london_airport_flights.requests.get", return_value=mock_response):
        result = make_get_request("http://example.com", {})

    assert result == payload
