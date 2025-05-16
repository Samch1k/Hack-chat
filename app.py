import chainlit as cl
import os
from dotenv import load_dotenv

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain_openai import OpenAI  # <-- новая библиотека

# Загружаем переменные окружения
load_dotenv()

# Выводим строку подключения для отладки
print("DATABASE_URL:", repr(os.getenv("DATABASE_URL")))

# Подключение к базе Supabase (через Connection Pooling или обычный URI)
db = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))

# Инициализация LLM (ключ берется из ENV: OPENAI_API_KEY)
llm = OpenAI(temperature=0)

# Создание SQL-агента
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# Обработка сообщений от пользователя
@cl.on_message
async def main(message: cl.Message):
    try:
        response = agent_executor.run(message.content)
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
