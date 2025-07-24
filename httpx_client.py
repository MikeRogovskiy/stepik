import httpx

data = {
  "email": "user@example.com",
  "password": "string"
}
response_login = httpx.post('http://localhost:8000/api/v1/authentication/login', json=data)

response_login_acc = response_login.json()
print(response_login_acc)

client = httpx.Client(base_url='http://localhost:8000', headers={
    "Authorization": f"Bearer {response_login_acc['token']['accessToken']}"
})

me_response = client.get('/api/v1/users/me')
me_response_data = me_response.json()
print(me_response_data)