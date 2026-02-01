import httpx
from httpx import QueryParams
from pathlib import Path

BASE_URL = "https://jsonplaceholder.typicode.com"
TODO_ID = 1
TODO_URL = f"{BASE_URL}/todos/{TODO_ID}"
TODOS_URL = f"{BASE_URL}/todos"
URL_HTTPBIN_ORG_BASE = "http://localhost:8080/"
HTTPBIN_ORG_POST = "post"
HTTPBIN_ORG_GET = "get"

response = httpx.get(TODO_URL)
print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post(TODOS_URL, json=data)
print(response.status_code)
print(response.json())

data = {
    "username": "test_user",
    "password": "12345",
}
response = httpx.post(f"{URL_HTTPBIN_ORG_BASE}{HTTPBIN_ORG_POST}", data=data)
print(response.status_code)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get(f"{URL_HTTPBIN_ORG_BASE}{HTTPBIN_ORG_GET}", headers=headers)

print(response.request.headers)
print(response.json())

# или
# params = QueryParams(userId=1)
params = {"userId": 1}
response = httpx.get(TODOS_URL, params=params)
print(response.url)
print(response.json())

with open("example.txt", "rb") as file:
    files = {
        "file": ("example.txt", file)
    }
    response = httpx.post(f"{URL_HTTPBIN_ORG_BASE}{HTTPBIN_ORG_POST}", files=files)
    print(response.json())
# или from pathlib import Path
# file_1 = Path("example.txt").read_bytes()
# files = {
#     "file1": ("example.txt", file_1)
# }
# response = httpx.post(f"{URL_HTTPBIN_ORG_BASE}{HTTPBIN_ORG_POST}", files=files)
# print(response.json())

with httpx.Client() as client:
    response1 = client.get(TODOS_URL + "/1")
    response2 = client.get(TODOS_URL + "/2")

print(response1.json())
print(response2.json())

client = httpx.Client(headers=headers)
response = client.get(f"{URL_HTTPBIN_ORG_BASE}{HTTPBIN_ORG_GET}")
print(response.json())
client.close()

try:
    response = httpx.get(TODOS_URL + "/invalidurl")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
