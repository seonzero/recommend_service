import streamlit as st

st.title("JPOP 추천 서비스")

#네비게이션 작성
index_page = st.Page("app/pages/index_page.py", title="홈페이지", icon="🏠")

pg = st.navigation([index_page])
pg.run()