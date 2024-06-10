import streamlit as st

# アプリのタイトル
st.title('文字数・単語数カウンター')

# ユーザーからの入力を受け取るテキストエリア
user_input = st.text_area("テキストを入力してください:")

# 入力されたテキストの文字数をカウント
char_count = len(user_input)

# 入力されたテキストの単語数をカウント
word_count = len(user_input.split())

# 結果を表示
st.write(f'入力されたテキストの文字数: {char_count}')
st.write(f'入力されたテキストの単語数: {word_count}')

