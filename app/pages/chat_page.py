# 환경 및 세션 준비
import os
import streamlit as st

# 0) api 키 불러오기
_api_key = st.secrets.get("GOOGLE_API_KEY", "")
if _api_key:
    os.environ.setdefault("GOOGLE_API_KEY", _api_key)
else:
    st.warning("GOOGLE_API_KEY 환경 변수가 설정되지 않았습니다.")


# 1) 세션 초기화
# - 전체 대화 정보 세션 - 모델을 통해 얻은 대화 맥락 관리 세션
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_memory" not in st.session_state:
    st.session_state.chat_memory = {} #딕셔너리 - 사용자식별자에 따라 서로 다른 맥락 관리를 위함