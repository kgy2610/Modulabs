# blog/views.py
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# 최소한의 동작을 하는 Post모델에 대한 View(Class Based View 활용)
# - .as_view 호출을 통해, View 함수를 만들어주는 클래스

# 설정보다는 관례

# 목록 조회 : 모델 클래스

post_list = ListView.as_view(
    model=Post,  # 필수
    # 생략하면, "앱이름/모델명소문자_list.html" 을 자동으로 찾아요.
    # template_name="blog/post_list.html",
)

# 단건 조회 : 모델 클래스

post_detail = DetailView.as_view(
    model=Post,
)

# 생성 : 모델 클래스, 폼 클래스

from blog.forms import CommentForm
from blog.models import Comment

# View 구현에서 반복을 줄일 수 있도록 도와주는 장고의 기능 : Class Based View

# comment_new = CreateView.as_view(
#     model=Comment,
#     form_class=CommentForm,
#     success_url="/blog/",  # TODO: 포스팅 detail 로 이동.
# )

# Form 요청을 위해, 하나의 주소에서 GET 요청과 POST 요청을 같이 받습니다. ==> Django Style
# - django도 주소에 기반해서 호출된 View를 매핑 => 하나의 주소 => 하나의 View
# - java spring : /blog/comments/form/ GET 요청 /blog/comments/submit/ POST 요청
#                 2개의 함수를 구현하게 되는거죠.

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    # html <form> 요청에서는 method는 단 2가지 : GET or POST (항상 대문자)
    # <form method="post">라고 썼다고 해도, 장고 서버에서는 항상 대문자.

    if request.method == "GET" :
        form = CommentForm()

    else: # POST
        # 제출받은 값들을 장고 Form에게 제출
        # Django View에서 요청받은 데이터 참조하는 법
        # 1) request.GET
        # 2) request.POST : 파일을 제외한 POST 데이터
        # 3) request.FILES : 파일로만 구성된 POST 데이터
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # django Form은 아래의 사전을 생성해주는 것까지가 책임의 끝.
            # - No DB 저장
            # form.cleaned_data # dict 타입 : 유효성 검사에 통과한 값들
            # django ModelForm: +DB로의 저장도 지원 (save 메서드 지원)
            saved_comment: Comment = form.save()
            # 대개의 서비스 기획 : 생성 폼에서 생성 성공하면, 다른 페이지로 이동
            post_url = f"/blog/{post_pk}/" # python, f-string 문법
            return redirect(post_url) # 브라우저에게 이동을 하라고, 지시

    return render(request, "blog/comment_form.html", {
        "form": form,
    })

# 수정 : 모델 클래스, 폼 클래스

# 삭제 : 모델 클래스