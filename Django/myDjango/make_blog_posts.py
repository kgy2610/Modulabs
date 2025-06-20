# 이 파일은 장고 프로젝트 외적인 파일입니다.
# 장고 밖에서 장고의 리소스를 활용해보고
# LLM을 통해서 블로그 포스팅을 생성해보겠습니다.

# 모든 장고를 활용하려는 파이썬 코드는 무조건 DJANGO_SETTINGS_MODULE 환경변수 지정이 필요합니다.
# 현재의 파이썬 코드를 통해 사용할 settings의 경로를 알려줘야만 합니다.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# 이제 장고 리소스를 활용할 준비가 끝났습니다.
# from blog.models import Post
# qs = Post.objects.all()
# print("post: ", qs)

from pyhub.llm import OpenAILLM, UpstageLLM
from pydantic import BaseModel
from django.conf import settings
from blog.models import Post

class BlogPost(BaseModel):
    title: str
    content: str

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    model='gpt-4o-mini',
    system_prompt="""
                    너는 평화로움과 자유를 추구하는 여행 블로거야.
                    유저가 제시하는 내용에 맞춰 블로그의 제목과 내용을 작성해줘.
                  """,
    max_tokens=8000, # default: 1000 (최대 : ??)
)

keywords = ["대전 성심당의 보문산 메아리",
            "대전 성심당의 먹물방망이",
            "대전 성심당의 야채고로케",
            "대전 성심당의 부추빵",
            "대전 성심당의 옥수수식빵",
            ]
# 블로그 포스트를 한 번에 10개 생성
for keyword in keywords:
    # ask : 모든 답변이 생성된 후 출력
    reply = llm.ask(
                keyword,
                schema=BlogPost,
                # pyhub-llm 내부에서 자동으로 대화 내역을 관리합니다.
                # 현재의 요청은 대화내역 관리가 필요 없으므로, 이 옵션을 지정해주세요.
                use_history=False,
            )
    print(reply)
    blog_post: BlogPost = reply.structured_data
    # blog_post.title  # str
    # blog_post.content  # str

    post = Post()
    post.title = blog_post.title
    post.content = blog_post.content
    post.save()

    print("saved post #", post.id)