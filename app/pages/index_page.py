import streamlit as st

#전체 요소를 가운데 정렬, 비율1:10:1
_, main, _ = st.columns([1,10,1])

with main:
    #이미지 가운데 정렬, 비율1:1:1
    _, image, _ = st.columns([1,1,1])
    with image:
        st.image("static/cherry.svg", width=200)

    #로고 아래 설명 문구 작성
    st.markdown(
        """
        ### 당신에게 딱 맞는 음악을 찾아드립니다. 
        - 레몬부터 사쿠란보까지! 
        """
    )