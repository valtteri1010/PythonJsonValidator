import requests

JSON_URL = "https://jsonplaceholder.typicode.com/todos/1"
expected_response = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

def check_response():
    response = requests.get(JSON_URL)
    if response.status_code != 200:
        print(f"Failed: Expected status 200, got {response.status_code}")
        return False

    data = response.json()
    passed = True

    for key, expected_value in expected_response.items():
        actual_value = data.get(key)
        if actual_value != expected_value:
            print(f"Mismatch on '{key}': expected {expected_value!r}, got {actual_value!r}")
            passed = False

    if passed:
        print("Test passed")
    else:
        print("Test failed")

    return passed

def test_api_response():
    assert check_response(), "API response did not match expected values"

def main():
    check_response()

if __name__ == "__main__":
    main()
