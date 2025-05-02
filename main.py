import pytest
import requests
from jsonschema import validate, ValidationError
from testCases import TEST_CASES

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request to {url} failed: {e}")
    except ValueError:
        pytest.fail(f"Invalid JSON received from {url}")

def test_api_schema_validation():
    for url, case in TEST_CASES:
        data = fetch_json(url)
        schema = case["schema"]
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            pytest.fail(f"[{url}] Schema validation error: {e.message}")

def test_api_field_values():
    for url, case in TEST_CASES:
        try:
            data = fetch_json(url)
        except pytest.fail.Exception as e:
            pytest.fail(f"[{url}] Fetch JSON failed: {e}")
        for key, expected_value in case["expected_values"].items():
            if expected_value is not None:
                actual_value = data.get(key)
                assert actual_value == expected_value, (
                    f"[{url}] Value mismatch on '{key}': "
                    f"expected {expected_value!r}, got {actual_value!r}"
                )