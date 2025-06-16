# 1) 라이브러리 설치 : openai
# pip install -U openai -> 이미 openai 라이브러리가 설치되어있더라도, 새로운 버전이 있다면 설치하세요.
# python -m pip install ~ (추천)
# => 기존 명령어는 가상환경이 달라 설치 오류가 발생할 수 있음
# 2) API KEY 미지정
# 3) 실행 명령어 python .\10.openai.py(파일명)
# 4) 깃 커밋시 api_key 삭제
from openai import OpenAI
client = OpenAI(api_key="")
# client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "hello"
        }
    ]
)

print(completion.choices[0].message.content)

# 경로 구분자 : 디렉토리 간 구분자
# - 윈도우 : 역슬래시 \
# - 맥/리눅스 : 슬래시/