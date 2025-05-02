import pytest
import requests
from testCases import TEST_CASES



def check_response(url, expected_response):
    print(f"Testing URL: {url}")
    try:
        response = requests.get(url)
    except Exception as e:
        print(f" Request failed: {e}")
        return False

    if response.status_code != 200:
        print(f" Failed: Expected status 200, got {response.status_code}")
        return False

    data = response.json()
    passed = True

    for key, (expected_value, expected_type) in expected_response.items():
        actual_value = data.get(key)

        if not isinstance(actual_value, expected_type):
            print(f" Type mismatch on '{key}': expected {expected_type.__name__}, got {type(actual_value).__name__}")
            passed = False
            continue

        if expected_value is not None and actual_value != expected_value:
            print(f" Value mismatch on '{key}': expected {expected_value!r}, got {actual_value!r}")
            passed = False

    if passed:
        print(" Test passed\n")
    else:
        print(" Test failed\n")

    return passed


def test_api_responses():
    failures = []

    for url, expected_response in TEST_CASES:
        passed = check_response(url, expected_response)
        if not passed:
            failures.append(url)

    if failures:
        failed_list = "\n".join(f" - {url}" for url in failures)
        pytest.fail(f"The following tests failed:\n{failed_list}")


def main():
    all_passed = True
    for url, expected_response in TEST_CASES:
        if not check_response(url, expected_response):
            all_passed = False
    if not all_passed:
        exit(1)


if __name__ == "__main__":
    main()
