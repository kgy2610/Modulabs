from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
blogs = ["블로그1번", "블로그2번","블로그3번"]

@app.get("/")
def index():
    return {"인사말": "안녕하세요."}


@app.get("/blog")
def blog_list():
    return {"목록": blogs}
    
# @app.get("/blog{post_id}") # blog/1     blog2
# def blog_detail(post_id: int):
#     return {"게시물 번호" : post_id}

@app.get("/blog/{post_tag}")
def tag_list(post:str):
    b = []
    for blog in blogs:
        if post_tag in blog:
            b.append(blog)

    return {"블로그(태그) 목록": b}


@app.get("/blog/{post_tag}/{post_author}")
def tag_author_list(post_tag: str, post_author: str):
    return {"태그": post_tag, "저자": post_author}

