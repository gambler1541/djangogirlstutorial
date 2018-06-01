from django.conf.urls import url

from .views import post_list

urlpatterns =[
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
    #   -> request를 받아서 response를 돌려주는 함수
    # blog.views에 있는 post_list함수를
    # 아래 url함수의 두 번째 인자로 전달
    # (함수호출 아님)
    url(r'^$',post_list),
]


