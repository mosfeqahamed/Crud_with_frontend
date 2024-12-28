import requests

URL = "http://127.0.0.1:8000/teacher/"

response = requests.get(url=URL)
print(response)
data = response.json()
print(data)