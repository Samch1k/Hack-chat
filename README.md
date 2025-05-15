# Oracle Chainlit

AI чат-бот на основе Chainlit, LangChain, Supabase и OpenAI.

## Запуск локально

```bash
pip install -r requirements.txt
chainlit run app.py
```

## Деплой на Railway

1. Подключи репозиторий на https://railway.app
2. Укажи build command:

```bash
pip install -r requirements.txt
```

3. Укажи start command:

```bash
chainlit run app.py --host 0.0.0.0 --port $PORT
```

4. Добавь переменные окружения:

- `OPENAI_API_KEY`
- `DATABASE_URL`

После деплоя получишь публичную ссылку.