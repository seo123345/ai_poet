#pip install pyton-dotenv
#pip install langchain-openai
#pip install streamlit
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject="AI"
# result=chat_model.invoke(subject+"에 대한 시를 써줘.")
# print(result.content)

import streamlit as st
st.title("인공지능 시인")
subject=st.text_input("시의 주제를 입력해주세요/\.")
st.write(subject)