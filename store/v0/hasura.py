import requests

# URL эндпоинта
url = "https://viable-pigeon-72.hasura.app/api/rest/products"

# Заголовки для авторизации
headers = {
    "x-hasura-admin-secret": "4tqWHzTodx7KVvoTDRSJa1o995X1sA6NN52ydz1Xx6fRdKxafi8CAExAuNTE2eci",
    "Content-Type": "application/json",
}

# Отправка GET-запроса
response = requests.get(url, headers=headers)

# Проверка ответа
if response.status_code == 200:
    data = response.json()
    print("Data:", data)
else:
    print(f"Failed to fetch data: {response.status_code}")
    print("Response:", response.text)
