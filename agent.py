# agent.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 创建客户端
client = OpenAI(api_key=api_key)

def ask_agent(prompt):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 或 "gpt-4"
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return chat_completion.choices[0].message.content.strip()

def main():
    print("欢迎使用你的简易Agent，输入 'exit' 退出。")
    while True:
        user_input = input("你：")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = ask_agent(user_input)
        print("Agent：", reply)

if __name__ == "__main__":
    main()

