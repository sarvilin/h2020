import requests
response = requests.get('https://ya.ru/white')
print(response.text)  # печатаем текст запрошенной страницы
