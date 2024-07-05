# Используйте официальный образ Python в качестве базового
FROM python:3.12-slim

# Установите зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Создайте и используйте рабочую директорию
WORKDIR /app

# Скопируйте зависимости проекта
COPY requirements.txt .

# Установите зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте содержимое проекта в рабочую директорию
COPY . .

# Установите переменные окружения
ENV DJANGO_SETTINGS_MODULE=jobsearch.settings

# Выполните миграции базы данных
RUN python manage.py migrate

# Соберите статические файлы
RUN python manage.py collectstatic --noinput

# Запустите сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
