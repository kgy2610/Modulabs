# baemin/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm

# 최신의 가게 목록 페이지를 보여줄 거예요.
#  - 최신의 데이터는 DB 안에 있죠. 그러니 매번 DB 조회를 할 겁니다.
def shop_list(request):
    # 데이터베이스에서 baemin_shop 테이블의 모든 레코드를
    # 조회할 준비 (아직 데이터를 가져오진 않았습니다.)
    qs = Shop.objects.all()  # QuerySet

    return render(
        request,
        template_name="baemin/shop_list.html",
        context={
            "shop_list": qs,
        })

# TODO: baemin/shop_list.html 템플릿을 만들어보기. 하얀 배경도 OK. chatgpt 등을 통한 코드 생성도 OK.

def shop_detail(request, pk):
    # DB에서 조회했습니다.
    shop = Shop.objects.get(pk=pk)    # 이 필드명 지정이 좀 더 정확한 네이밍.
    # shop = Shop.objects.get(id=pk)  # 위와 동일한 동작

    # 전체(모든 shop) 리뷰 데이터를 가져올 준비
    review_qs = Review.objects.all()
    review_qs = review_qs.filter(shop=shop)
    
    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={
            "shop": shop,
            "reviews": review_qs,
            },
        )

# TODO: baemin/shop_detail.html 템플릿을 만들어보기.

def review_new(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop  # 어떤 가게에 대한 리뷰인지 저장
            review.save()
            return redirect(f"/baemin/{shop.pk}/")
    else:
        form = ReviewForm()

    return render(
        request,
        "baemin/review_form.html",
        {
            "shop": shop,
            "form": form,
        }
    )