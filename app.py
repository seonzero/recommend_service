import streamlit as st

st.title("JPOP 추천 서비스")

#네비게이션 작성
#홈페이지
index_page = st.Page("app/pages/index_page.py", title="홈페이지", icon="🏠")
#로그인
login_page = st.Page("app/pages/login_page.py", title="로그인", icon="🔒")

#네이게이션 리스트
pg = st.navigation([index_page, login_page])
pg.run()