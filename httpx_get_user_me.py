import httpx

data = {
  "email": "user@example.com",
  "password": "string"
}
response_login = httpx.post('http://localhost:8000/api/v1/authentication/login', json=data)

response_login_acc = response_login.json()
print(response_login_acc)
print(response_login.status_code)


headers = {
    "Authorization": f"Bearer {response_login_acc['token']["accessToken"]}"
}

response_me = httpx.get('http://localhost:8000/api/v1/users/me', headers= headers )

print(response_me.json())
print(response_me.status_code)
