import httpx

base_url = "http://localhost:8000"

login_data = {
  "email": "user@example.com",
  "password": "string"
}
login_response = httpx.post(f'{base_url}/api/v1/authentication/login', json=login_data)
"""Запрос аутентификацию /api/v1/authentication/login"""

access_token = login_response.json()["token"]["accessToken"]
""" Токен из ответа /api/v1/authentication/login"""

user_me_response = httpx.get(f'{base_url}/api/v1/users/me', headers={"Authorization": f"Bearer {access_token}"})
print(user_me_response.status_code)
print(user_me_response.json())





