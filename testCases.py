TEST_CASES = [
    (
        "https://jsonplaceholder.typicode.com/todos/1",
        {
            "schema": {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "completed": {"type": "boolean"}
                },
                "required": ["userId", "id", "title", "completed"]
            },
            "expected_values": {
                "userId": None,  # Accept any int
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
            }
        }
    ),
    (
        "https://jsonplaceholder.typicode.com/todos/2",
        {
            "schema": {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "completed": {"type": "boolean"}
                },
                "required": ["userId", "id", "title", "completed"]
            },
            "expected_values": {
                "userId": 1,
                "id": 2,
                "title": "quis ut nam facilis et officia qui",
                "completed": False
            }
        }
    ),
(
        "https://jsonplaceholder.typicode.com/todos/3",
        {
            "schema": {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "completed": {"type": "boolean"}
                },
                "required": ["userId", "id", "title", "completed"]
            },
            "expected_values": {
                "userId": 1,
                "id": 3,
                "title": "fugiat veniam minus",
                "completed": False
            }
        }
    ),
(
        "https://jsonplaceholder.typicode.com/todos/4",
        {
            "schema": {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "completed": {"type": "boolean"}
                },
                "required": ["userId", "id", "title", "completed"]
            },
            "expected_values": {
                "userId": 1,
                "id": 4,
                "title": "et porro tempora",
                "completed": True
            }
        }
    ),
]
