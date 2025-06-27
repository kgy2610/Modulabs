# blog/admin.py

from django.contrib import admin
from .models import Post, Comment

# 모델을 admin에 등록하는 첫 번째 방법
# - 디폴트 admin 옵션으로 등록할 때
# admin.site.register(Post)

# 두 번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass
# 리스트에 노출되는 내용을 커스텀 할 수 있다

# admin.site.register(Post, PostAdmin)


# 세 번째 방법
# @: 장식자 => 코드를 장식하여 새로운 클래스를 생성해라
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    search_fields = ["title"]
    list_filter = ["status"]

admin.site.register(Comment)
