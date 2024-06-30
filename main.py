import requests

# # Параметры запроса
# params = {
#     'text': 'python',  # Поиск по ключевому слову
#     'area': '1',        # Регион поиска (например, Москва)
#     'per_page': 3
# }
#
# # Выполнение запроса
# response = requests.get('https://api.hh.ru/vacancies', params=params)
#
# # Проверка статуса ответа и вывод данных
# if response.status_code == 200:
#     vacancies = response.json()
#     print(vacancies)
# else:
#     print(f'Error: {response.status_code}')
# import requests

# ID вакансии
vacancy_id = '4195968'

# Выполнение запроса
response = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')

# Проверка статуса ответа и вывод данных
if response.status_code == 200:
    vacancy_details = response.json()
    print(vacancy_details)
else:
    print(f'Error: {response.status_code}')
import requests

# ID вакансии
vacancy_id = '102757997'

# Выполнение запроса
response = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')

# Проверка статуса ответа и вывод данных
if response.status_code == 200:
    vacancy_details = response.json()
    print(vacancy_details)
else:
    print(f'Error: {response.status_code}')
