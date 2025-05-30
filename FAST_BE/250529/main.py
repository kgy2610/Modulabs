from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
notices = ["공지사항1", "공지사항2", "공지사항3"]
templates = Jinja2Templates(directory="templates")  # templates 폴더를 지정합니다.


@app.get("/")  # -> 127.0.0.1:8000 get method
def read_root():
    return {"Hello": "World!"}


@app.get("/about")  # -> 127.0.0.1:8000/about get method
def about():
    return {"message": "about page"}


@app.get("/contact")  # -> 127.0.0.1:8000/contact get method
def contact():
    return {"message": "contact page"}


@app.get("/notice")  # -> 127.0.0.1:8000/notice get method
def notice():
    return {"notice": notices}


@app.get("/index", response_class=HTMLResponse)
def index():
    return "<h1> 안녕하세요! </h1>"


@app.get("/index2") # -> 127.0.0.1:8000/index2 get method
def index2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/")
# def post_root():
#     return {"이건":"포스트입니다."}

# @app.get("/good")
# def read_good():
#     return {"a": 1}

# @app.get("/users")
# def get_users():
#     return {"a": 1, "b": 2}

# # 실습
# # get /todo -> 아무데이터 반환,
# # get 주소는 자유 -> 아무데이터 반환

# @app.get("/todo")
# def read_todo():
#     return {"할 일" : "복습하기"}

# @app.get("/hello")
# def hello():
#     return {"message" : "안녕하세요"}