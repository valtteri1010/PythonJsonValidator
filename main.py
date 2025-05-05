import pytest
import requests
from jsonschema import validate, ValidationError
from testCases import TEST_CASES

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.RequestException as e:
        return None, f"Request to {url} failed: {e}"
    except ValueError:
        return None, f"Invalid JSON received from {url}"

@pytest.mark.parametrize("url,case", TEST_CASES)
def test_api_schema_validation(url, case):
    data, error = fetch_json(url)
    assert not error, f"[{url}] Fetch error: {error}"

    schema = case["schema"]
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        pytest.fail(f"[{url}] Schema validation error: {e.message}")

@pytest.mark.parametrize("url,case", TEST_CASES)
def test_api_field_values(url, case):
    data, error = fetch_json(url)
    assert not error, f"[{url}] Fetch error: {error}"

    for key, expected_value in case["expected_values"].items():
        if expected_value is not None:
            actual_value = data.get(key)
            assert actual_value == expected_value, (
                f"[{url}] Value mismatch on '{key}': expected {expected_value!r}, got {actual_value!r}"
            )
