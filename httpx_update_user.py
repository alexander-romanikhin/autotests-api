import httpx
from tools.fakers import *

base_url = "http://localhost:8000"

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(f'{base_url}/api/v1/users', json=create_user_payload) # Запрос на создание юзера

create_user_response_data = create_user_response.json() # Сохраняем ответа по созданию
user_id = create_user_response_data['user']['id'] # Сохраняем идентификатор пользователя
print("Create user status code: ", create_user_response.status_code)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
# Отправляем запрос на логин и вытаскиваем токен
login_response = httpx.post(f'{base_url}/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('Login data: ', login_response_data)
print("Login status code: ", login_response.status_code)
login_bearer_token = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
# Формируем пэйлоад с ранодмными значениями
update_user_payload = {
  "email": get_random_email(),
  "lastName": get_random_surname(),
  "firstName": get_random_username(),
  "middleName": get_random_middle_name()
}

# Отправляем запрос на обновление данных пользователя
update_user_response = httpx.patch(f'{base_url}/api/v1/users/{user_id}', headers=login_bearer_token, json=update_user_payload)

print("Update user status code: ", update_user_response.status_code)