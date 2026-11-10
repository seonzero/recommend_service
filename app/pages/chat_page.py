# 환경 및 세션 준비
import os
import streamlit as st
# 대화 내역 관리
from langchain_core.chat_history import InMemoryChatMessageHistory
# llm 체인 구성
from langchain_google_genai import ChatGoogleGenerativeAI #모델
from langchain_core.output_parsers import StrOutputParser #파서
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder #프롬프트
from langchain_core.runnables.history import RunnableWithMessageHistory #연결
# 라우터 구성
from langchain_core.runnables import RunnableLambda


st.subheader("💬 AI Chatbot")


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

#🧠대화 내역 저장소
# - RunnableWithMessageHistory 객체 생성시 사용할 함수 
# : 사용자 식별키에 따라 적절한 대화 내용 저장소 생성 or 반환
# 이때 대화내용저장소(chat_memory)는 InMemoryChatMessageHistory 객체로 생성
def get_memory(session_id):
    session_key = session_id or SESSION_ID
    chat_memories = st.session_state.chat_memory
    if session_key not in chat_memories:
        chat_memories[session_key] = InMemoryChatMessageHistory()
    return chat_memories[session_key]
#🧠InMemorychatMessageHistory()객체인 chat_memories[session_key]을 반환한다


# 2) 범용 답변용 구성 요소 정의와 체인 생성
# - 프롬프트, 모델, 출력 파서 정의
prompt = ChatPromptTemplate(
    [
        (
            "system",
            """
            너는 친절한 JPOP 리스너이다. 
            이전 메시지를 바탕으로 질문 의도를 파악하고, 단계적으로 설명하라.
            """,
        ),
        MessagesPlaceholder(variable_name = "history"), #history라는 변수
        ("human", "{input}"), #question이라는 변수
    ]
)
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
output_parser = StrOutputParser()

# 범용 답변 체인 생성
chain = prompt | model | output_parser

# - RunnableWithMessageHistory를 사용해 전체 흐름 정리 & 대화 내역 관리
#🧠 앞서 정의한 체인(chain)과 대화내역저장소(get_memory)를 하나로 묶어준다

general_chain = RunnableWithMessageHistory(
    chain, 
    get_memory, #🧠 대화내역저장소를 가져오는 함수
    input_message_key = "input",
    history_messages_key = "history",
)


# 라우터 구성
router_keywords = {
    "콘서트 검색": ["콘서트", "concert", "비용", "가려면", "티켓"], 
    "유튜브": ["유튜브", "youtube", "영상", "동영상"],
}

def classify_topic(user_input):
    for key, values in router_keywords.items():
        if any(keyword in user_input for keyword in values):
            return key
    return "기타"

def router_step(inputs):
    user_input = inputs["input"]
    topic = classify_topic(user_input)
    return {"input": user_input, "topic": topic}

# RunnableLambda 객체를 통해 중간 체인을 정의해준다. 
# 사용자 질문 내용에 따라 토픽이 결정되어 반환되는 중간 체인
router_chain = RunnableLambda(router_step)

# 넘겨받은 딕셔너리를 기반으로 서로 다른 답변이 실행될 수 있는 최종 route함수
def route(info):
    topic = info["topic"]
    if topic == "유튜브":
        return "유튜브 검색 기능은 향후 구현될 예정입니다."

    if topic == "콘서트 검색":
        return "콘서트 검색 기능은 향후 구현될 예정입니다."

    return general_chain.invoke(
        {"input": info["input"]},
        config={"session_id": SESSION_ID},
    )


# 3) 최종 체인 구성
full_chain = (
    router_chain #return: {"question": question, "topic": topic}
    | RunnableLambda(route)
)

# 4) 사용자 입력
prompt = st.chat_input("무엇을 도와드릴까요?")

# 5) 들어온 값 저장
if prompt:
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.spinner("AI가 응답을 생성하는 중입니다..."):
        response = full_chain.invoke({"input": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})

# 6) 출력
for message in st.session_state.messages:
    speaker = "user" if message["role"] == "user" else "assistant"

    with st.chat_message(speaker):
        st.markdown(message["content"])