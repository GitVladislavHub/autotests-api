import httpx
from tools.fakers import get_random_email

BASE_URL = "http://localhost:8000"
USERS_POST = "/api/v1/users"

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post(f"{BASE_URL}{USERS_POST}", json=payload)
print(f"Код ответа: {response.status_code}")
print(f"JSON: {response.json()}")
