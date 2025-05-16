# Используем лёгкий образ Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Обновляем pip и устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        chainlit==1.0.300 \
        langchain==0.1.16 \
        langchain-community==0.0.36 \
        langchain-openai==0.0.8 \
        openai==1.10.0 \
        psycopg2-binary==2.9.9 \
        python-dotenv==1.0.1 \
        "SQLAlchemy<2.0"

# Открываем порт (Railway автоматически использует 8000)
EXPOSE 8000

# Команда запуска Chainlit-приложения
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0",]()
