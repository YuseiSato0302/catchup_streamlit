import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# タイトルとサブヘッダー
st.title("Streamlit 入門")
st.subheader("基本的な機能紹介")

# # テキスト入力
# st.write("### テキスト入力")
# name = st.text_input("名前を入力してください")

# # 数値入力
# st.write("### 数値入力")
# age = st.number_input("年齢を入力してください", min_value=1, max_value=120)

# # ボタン
# if st.button("送信"):
#     st.write(f"こんにちは、{name}さん！あなたは{age}歳です。")

# # チェックボックス
# st.write("### チェックボックス")
# if st.checkbox("データを表示する"):
#     data = pd.DataFrame({
#         '列A': np.random.randn(100),
#         '列B': np.random.randn(100)
#     })
#     st.write(data)

# # セレクトボックス
# st.write("### セレクトボックス")
# option = st.selectbox(
#     "好きな色を選んでください",
#     ["赤", "青", "緑", "黄色"]
# )
# st.write("あなたの好きな色は", option, "です。")

# # スライダー
# st.write("### スライダー")
# value = st.slider("値を選んでください", 0, 100, 50)
# st.write("選択した値は", value, "です。")

# # プログレスバー
# st.write("### プログレスバー")
# import time

# progress_bar = st.progress(0)
# for i in range(100):
#     time.sleep(0.1)
#     progress_bar.progress(i + 1)

# # グラフ表示
# st.write("### グラフ表示")
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['列A', '列B', '列C']
# )
# st.line_chart(chart_data)

# # マップ表示
# st.write("### マップ表示")
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )
# st.map(map_data)

# # ファイルアップロード
# st.write("### ファイルアップロード")
# uploaded_file = st.file_uploader("ファイルを選択してください")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write(df)

# # サイドバー
# st.sidebar.title("サイドバー")
# st.sidebar.write("これはサイドバーの例です。")

# # マルチセレクト
# st.write("### マルチセレクト")
# options = st.multiselect(
#     "好きなフルーツを選んでください",
#     ["リンゴ", "バナナ", "オレンジ", "ブドウ", "メロン"]
# )
# st.write("選択したフルーツは", options, "です。")

# # テキストエリア
# st.write("### テキストエリア")
# text_area = st.text_area("メッセージを入力してください")
# st.write("入力したメッセージは以下です。")
# st.write(text_area)

# # カラーピッカー
# st.write("### カラーピッカー")
# color = st.color_picker("色を選んでください", "#00f900")
# st.write("選択した色は", color, "です。")
