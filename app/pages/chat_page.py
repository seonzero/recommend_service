# 환경 및 세션 준비
import os
import streamlit as st
# 대화 내역 관리
from langchain_core.chat_history import InMemoryChatMessageHistory

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

# 대화 내역 관리
# - session_id에 사용자 식별값 할당
SESSION_ID = "chapter6"

# - RunnableWithMessageHistory 객체 생성시 사용할 함수 
# : 사용자 식별키에 따라 적절한 대화 내용 저장소 생성 or 반환
# 이때 대화내용저장소(chat_memory)는 InMemoryChatMessageHistory 객체로 생성
def get_memory(session_id):
    session_key = session_id or SESSION_ID
    chat_memories = st.session_state.chat_memory
    if session_key not in chat_memories:
        chat_memories[session_key] = InMemoryChatMessageHistory()
    return chat_memories[session_key]

