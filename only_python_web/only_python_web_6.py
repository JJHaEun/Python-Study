# 사용자가 업로드한 엑셀 파일 시각화하기
import streamlit as st
from googletrans import Translator
import asyncio

async def main():
    translator = Translator()


    st.write("""
    # 번역 모델 v0.1
    입력된 텍스트를 영어로 번역합니다.
    """)

    txt = st.text_area("번역할 텍스트","""안녕하세요, 반갑습니다. 파이썬은 재미있나요?""")
    translater_txt = await translator.translate(txt,dest="en",src="ko")
    st.write("번역 결과:", translater_txt.text)

asyncio.run(main())
# streamlit run only_python_web_5.py 