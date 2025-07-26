# web_agent.py

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# 读取 API key
#load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#client = OpenAI(api_key=api_key)

# 使用 st.secrets 获取 API 密钥（来自部署配置）
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Web AI Agent", page_icon="🤖")
st.title("🤖 你的 Web AI Agent")

# 会话状态用于保存对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 用户输入
user_input = st.chat_input("说点什么...")

if user_input:
    # 显示用户输入
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 调用模型
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"[错误] {e}"

    # 显示助手回复
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

