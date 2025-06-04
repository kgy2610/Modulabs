"""
사용자 등록 API 만들기

사용자 정보를 등록할 수 있는 POST API를 FastAPI로 만들어보세요.
사용자 정보는 이름(name: 문자열), 나이(age: 정수)로 구성되어 있습니다.

[ 조건 ]
- Pydantic의 BaseModel을 사용하여 사용자 입력을 검증,
- POST 요청으로 사용자 데이터를 받으면, 다음과 같은 응답을 JSON으로 반환

{"message": "홍길동님, 등록이 완료되었습니다."}
출력 예시
POST /users
Body:
{
    "name": "홍길동",
    "age": 25
}

Response:
{
    "message": "홍길동님, 등록이 완료되었습니다."
}
"""
from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

from typing import List

app = FastAPI()

# 사용자 정보 모델 정의
class User(BaseModel):
    name: str
    age: int

# 사용자 등록 API
@app.post("/users")
def register_user(user: User):
    return {
        "message": f"{user.name}님, 등록이 완료되었습니다."
        }

"""
나이로 사용자 필터링 API
여러 명의 사용자 정보가 리스트로 주어졌을 때, 입력한 나이 이상인 사용자들만 필터링하여 반환하는 GET API를 만드세요.

[ 조건 ]
- 사용자 정보는 서버 내에서 고정된 리스트로 관리 (DB 없이 in-memory),
- /users?min_age=30처럼 쿼리 파라미터로 나이 기준을 입력받기,
- min_age 이상인 사용자들의 리스트를 반환

# 내부 사용자 데이터
[
    {"name": "홍길동", "age": 25},
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]

# GET /users?min_age=30
# Response:
[
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]
"""
users_data = [
    {"name": "홍길동", "age": 25},
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]

# 사용자 나이 기준 필터링
@app.get("/users")
def get_users(min_age: int = Query(..., description="최소 나이")):
    """
    min_age 이상인 사용자만 필터링
    ... : 쿼리 파라미터로 입력 받아야함, 주소에 ?min_age=20 필수 포함 요청청
    """
    filtered_users = [user for user in users_data if user["age"] >= min_age]
    return filtered_users