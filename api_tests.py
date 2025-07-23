import httpx

payload = {
  "email": "user@example.com",
  "password": "string"
}

response_authentification = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload)
response_auth = response_authentification.json()

print(response_authentification.json())

refresh_payload = {
    "refreshToken":response_auth['token']['refreshToken']
}

response_refresh = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)

print(response_refresh.json())
