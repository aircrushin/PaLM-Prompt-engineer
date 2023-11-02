import streamlit as st
import google.generativeai as palm
import prompts 
import os
import pyperclip
from time import sleep

os.environ["HTTP_PROXY"] = "http://127.0.0.1:33210"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:33210"
#proxies = {'http': "socks5://127.0.0.1:33211",'https': "socks5://127.0.0.1:33211"}
api_key = 'AIzaSyAyP1wCoBuCgO5w5hX4zTudqN9x9Y34Izo'
palm.configure(api_key=api_key)

#function zone
def copy_text(text):
    pyperclip.copy(text)

#default configs
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.5,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}

#test input
input = 'I want to visit Chengdu, please give me some advice'

# 创建一个空的聊天历史记录列表
chat_history = []

# 定义Streamlit应用的标题
st.title("Prompt Engineer")

# 创建一个文本框用于用户输入
user_input = st.chat_input(placeholder='请输入Prompt', key=len(chat_history))

# 当用户点击“发送”按钮时，将用户输入添加到聊天历史记录中
if user_input:
    chat_history.append(("You", user_input))

# 显示聊天历史记录
for sender, message in chat_history:
    with st.chat_message(name='user'):
        st.write(f"{sender}: {message}")

# 示例回复
if chat_history:
    response = palm.generate_text(
        **defaults,
        prompt = prompts.prompt + user_input,
    )
    if response:
        sleep(0.5)
        with st.chat_message(name='model'):
            st.write(response.result)
            copy_text(response.result)
