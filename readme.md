## 사전 준비물
- python 3.11 이상
- gemini api 키
- git, pip 사용 가능 환경

## 설치 방법
1. 저장소 복제 or 소스코드 다운
2. 가상환경을 만들고 활성화
```bash
python -m venv .venv
source .venv/Scripts/activate
```
3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 과정
- app.py

- 인덱스 페이지 생성
    ![인덱스페이지](readme_image/index_page.png)

- 로그인 페이지 작성
    ![alt text](readme_image/login_page_1.png)
    ![alt text](readme_image/login_page_2.png)

- ai 챗봇 페이지 작성 
    (본격적 기능 구현 전 간단 페이지만 생성)
    ![alt text](readme_image/chat_page.png)

## 여담
- 메모리 이슈...
    
    어라? 이전 대화가 없어서 아직 성함(닉네임)을 잘 모르겠어요! 😅
    ![alt text](readme_image/error_no_memory.png)

- 랭체인 환경변수 여부에 따라 변수명을 `question`에서 `input`으로 바꿔야했다. (chat_page 구조 자체는 문제없었다)
    ![alt text](readme_image/error_complete_no_message.png)