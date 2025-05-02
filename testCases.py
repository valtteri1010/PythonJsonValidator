# (expected_value, expected_type)
TEST_CASES = [
    (
        "https://jsonplaceholder.typicode.com/todos/1",
        {
            "userId": (None, int),
            "id": (None, int),
            "title": ("delectus aut autem", str),
            "completed": (False, bool)
        }
    ),
    (
        "https://jsonplaceholder.typicode.com/todos/2",
        {
            "userId": (1, int),
            "id": (2, int),
            "title": ("quis ut nam facilis et officia qui", str),
            "completed": (False, bool)
        }
    ),
(
        "https://jsonplaceholder.typicode.com/todos/3",
        {
            "userId": (None, int),
            "id": (None, int),
            "title": ("fugiat veniam minus", str),
            "completed": (False, bool)
        }
    ),
]