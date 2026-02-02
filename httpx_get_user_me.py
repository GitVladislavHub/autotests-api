import httpx

BASE_URL = "http://localhost:8000"
AUTHENTICATION_LOGIN_POST = "/api/v1/authentication/login"
AUTHENTICATION_REFRESH_TOKEN_POST = "/api/v1/authentication/refresh"
USERS_GET = "/api/v1/users/me"

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post(f"{BASE_URL}{AUTHENTICATION_LOGIN_POST}", json=login_payload)
login_response_data = login_response.json()

print("Код ответа для login:", login_response.status_code)
print("JSON для login:", login_response_data)

headers = {
    'Authorization': f'Bearer {login_response_data["token"]["accessToken"]}'
}
users_response = httpx.get(f"{BASE_URL}{USERS_GET}", headers=headers)
print(f"Код ответа для users: {users_response.status_code}")
print(f"JSON для users: {users_response.json()}")
