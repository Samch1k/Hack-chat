import chainlit as cl
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain_openai import OpenAI
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

print("DATABASE_URL:", os.getenv("DATABASE_URL"))  # Debug

db = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))
llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

@cl.on_message
async def main(message: cl.Message):
    try:
        response = agent_executor.run(message.content)
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
