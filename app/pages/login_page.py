import streamlit as st
#실제 로그인 기능 구현은 아니고
#간단한 입력 폼만 화면에 구성하고, 네이게이션에 등록하여 화면에 등록하기

st.subheader("로그인")
#입력창 구성: text_input 함수 사용
user_id = st.text_input("Id", key="login_id")
password = st.text_input("Password", type = "password", key="login_password")
#type속성을 password로 설정 - 사용자 입력값이 * 모양으로 마스킹됨

st.button("로그인", key="login_button")