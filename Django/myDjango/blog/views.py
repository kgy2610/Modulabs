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

comment_new = CreateView.as_view(
    model=Comment,
    form_class=CommentForm,
    success_url="/blog/",  # TODO: 포스팅 detail 로 이동.
)

# 수정 : 모델 클래스, 폼 클래스

# 삭제 : 모델 클래스