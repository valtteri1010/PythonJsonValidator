import pytest
import requests

TEST_CASES = [
    (
        "https://jsonplaceholder.typicode.com/todos/1",
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autems",
            "completed": False
        }
    ),
    (
        "https://jsonplaceholder.typicode.com/todos/2",
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        }
    ),
]


def check_response(url, expected_response):
    print(f"Testing URL: {url}")
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed: {e}")
        return False

    if response.status_code != 200:
        print(f"Failed: Expected status 200, got {response.status_code}")
        return False

    data = response.json()
    passed = True

    for key, expected_value in expected_response.items():
        actual_value = data.get(key)
        if actual_value != expected_value:
            print(f"  Mismatch on '{key}': expected {expected_value!r}, got {actual_value!r}")
            passed = False

    if passed:
        print("Test passed\n")
    else:
        print("Test failed\n")

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
