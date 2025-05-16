import chainlit as cl
import os
from dotenv import load_dotenv

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain_openai import OpenAI

load_dotenv()

print("DATABASE_URL:", repr(os.getenv("DATABASE_URL")))

db = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))
llm = OpenAI(temperature=0)  # <-- ключ берется из ENV

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

@cl.on_message
async def main(message: cl.Message):
    try:
        response = agent_executor.run(message.content)
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
