# Используем базовый образ с нужной версией Python
FROM python:3.8

# Устанавливаем переменные окружения для PostgreSQL
ENV POSTGRES_DB=your_database_name
ENV POSTGRES_USER=your_username
ENV POSTGRES_PASSWORD=your_password

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости (requirements.txt должен быть в текущей директории)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы приложения в контейнер
COPY . .

# Устанавливаем PostgreSQL (сервер)
RUN apt-get update && apt-get install -y postgresql

# Команда для запуска веб-приложения (PostgreSQL будет управляться через Docker Compose)
CMD ["python", "app.py"]
