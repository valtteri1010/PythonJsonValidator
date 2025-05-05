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


def test_api_schema_validation():
    errors = []
    for url, case in TEST_CASES:
        data, error = fetch_json(url)
        if error:
            errors.append(f"[{url}] Fetch error: {error}")
            continue

        schema = case["schema"]
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            errors.append(f"[{url}] Schema validation error: {e.message}")

    if errors:
        pytest.fail("\n".join(errors))


def test_api_field_values():
    errors = []
    for url, case in TEST_CASES:
        data, error = fetch_json(url)
        if error:
            errors.append(f"[{url}] Fetch error: {error}")
            continue

        for key, expected_value in case["expected_values"].items():
            if expected_value is not None:
                actual_value = data.get(key)
                if actual_value != expected_value:
                    errors.append(
                        f"[{url}] Value mismatch on '{key}': expected {expected_value!r}, got {actual_value!r}"
                    )

    if errors:
        pytest.fail("\n".join(errors))
