from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
items = []


class Item(BaseModel):
    name: str
    price: float = 0.0


@app.get("/item")
def item_list():
    return {"item": items}


@app.post("/item/create")
def create_item(item: Item):
    items.append(item)
    print(item.name, item.price)
    return {"item": item}

@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}

"""
1. 사용자 정보를 저장하는 POST 엔드포인트를 만들어보세요. 사용자 정보는 이름, 이메일, 나이를 포함해야 합니다.
Pydantic 모델을 사용하여 데이터를 검증하세요. -> 사용자정보리스트에 추가(people)
2. 사용자정보 리스트(people [list]) -> 조회하기
"""
# 사용자 정보 정의
class User(BaseModel):
    name: str
    email: str
    age: int


# 사용자 정보 리스트
people: List[User] = []


# 사용자 정보 저장(POST)
@app.post("/users")
def create_user(user: User):
    people.append(user)
    return {"message" : "사용자 정보가 저장되었습니다.", "user" : user}


@app.get("/users")
def get_users():
    return people


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    del users[user_id - 1]