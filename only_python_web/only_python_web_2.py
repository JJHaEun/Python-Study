# 파이썬만으로 웹사이트 그래프 띄우기
import streamlit as st
import pandas as pd


st.write("""
# 2022년 블로그 방문자수 추이
블로그 월 방문자수 추이 그래프입니다.\n
1월부터 11월까지
 """)

df = pd.read_excel("blog.xlsx")
st.line_chart(df)


# streamlit run only_python_web_1.py 