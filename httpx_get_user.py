import httpx
from tools.fakers import get_random_email

BASE_URL = "http://localhost:8000"
USERS = "/api/v1/users"
AUTHENTICATION_LOGIN = "/api/v1/authentication/login"

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(f"{BASE_URL}{USERS}", json=create_user_payload)
create_user_response_data = create_user_response.json()

print('Create user data', create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post(f"{BASE_URL}{AUTHENTICATION_LOGIN}", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

get_user_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(
    f"{BASE_URL}{USERS}/{create_user_response_data['user']['id']}",
    headers=get_user_header
)
get_user_response_data = get_user_response.json()
print('Get user data:', get_user_response_data)
