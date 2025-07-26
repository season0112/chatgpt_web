# gui_agent.py

import os
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv

# 载入 API 密钥
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 调用 Agent
def ask_agent(prompt):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content.strip()

# 提交用户输入并显示回复
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_window.insert(tk.END, "你: " + user_input + "\n", "user")
    entry.delete(0, tk.END)
    try:
        reply = ask_agent(user_input)
    except Exception as e:
        reply = f"[错误] {str(e)}"
    chat_window.insert(tk.END, "Agent: " + reply + "\n", "agent")
    chat_window.see(tk.END)

# 初始化界面
root = tk.Tk()
root.title("简易 AI Agent")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25)
chat_window.pack(padx=10, pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("agent", foreground="green")

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

# 回车键触发发送
root.bind('<Return>', lambda event=None: send_message())

root.mainloop()

