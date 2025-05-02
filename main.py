import pytest
import requests
from testCases import TEST_CASES

def fetch_json(url):
    try:
        response = requests.get(url)
    except Exception as e:
        pytest.fail(f"Request to {url} failed: {e}")
    if response.status_code != 200:
        pytest.fail(f"Expected status 200, got {response.status_code} from {url}")
    return response.json()


def test_api_field_types():
    for url, expected_fields in TEST_CASES:
        data = fetch_json(url)
        for key, (_, expected_type) in expected_fields.items():
            actual_value = data.get(key)
            assert isinstance(actual_value, expected_type), (
                f"[{url}] Type mismatch on '{key}': "
                f"expected {expected_type.__name__}, got {type(actual_value).__name__}"
            )


def test_api_field_values():
    for url, expected_fields in TEST_CASES:
        data = fetch_json(url)
        for key, (expected_value, _) in expected_fields.items():
            if expected_value is not None:  # Skip value check if None
                actual_value = data.get(key)
                assert actual_value == expected_value, (
                    f"[{url}] Value mismatch on '{key}': "
                    f"expected {expected_value!r}, got {actual_value!r}"
                )
