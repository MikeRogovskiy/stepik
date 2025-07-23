import httpx
from tools.fakers import random_email

create_payload = {
  "email": random_email(),
  "password": "123",
  "lastName": "st12ring",
  "firstName": "st2ring",
  "middleName": "str2ing"
}
create_response = httpx.post('http://localhost:8000/api/v1/users', json=create_payload)
create_resp = create_response.json()
print(create_resp)

login_payload = {
  "email": create_payload['email'],
  "password": create_payload["password"]
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_resp = login_response.json()
print(login_resp)




change_payload = {
  "email": random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

headers = {
    "Authorization": f"Bearer {login_resp["token"]["accessToken"]}"
}

change_response = httpx.patch(f'http://localhost:8000/api/v1/users/{create_resp['user']['id']}', json=change_payload, headers=headers)
change_resp = change_response.json()

print(change_resp)
print(change_response.status_code)
