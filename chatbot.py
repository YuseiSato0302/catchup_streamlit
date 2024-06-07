import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import os

# 環境変数からAPIキーを取得
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# APIキー設定
genai.configure(api_key=GOOGLE_API_KEY)

# タイトルを設定する
st.set_page_config(
    page_title="Chat with Gemini Pro",
    page_icon="🌮"
)

st.title("Chat with Gemini Pro")

# セッション状態の初期化
if "chat_session" not in st.session_state :
    model = genai.GenerativeModel('gemini-pro')
    st.session_state["chat_session"] = model.start_chat(history=[
        glm.Content(role="user", parts=[glm.Part(text="あなたは優秀なAIアシスタントです。できるだけ簡潔に回答してください。")]),
        glm.Content(role="model", parts=[glm.Part(text="わかりました。")])
    ])
    st.session_state["chat_history"] = []

# チャット履歴を全て表示
for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力送信後処理
if prompt := st.chat_input("ここに入力してください"):

    # ユーザの入力を表示する
    with st.chat_message("user"):
        st.markdown(prompt)

    # ユーザの入力をチャット履歴に追加する
    st.session_state["chat_history"].append({"role": "user", "content": prompt})

    # Genimi Proにメッセージ送信
    response = st.session_state["chat_session"].send_message(prompt)

    # Genimi Proのレスポンス表示
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Genimi Proのレスポンスをチャット履歴に追加する
    st.session_state["chat_history"].append({"role": "assistant", "content": response.text})
