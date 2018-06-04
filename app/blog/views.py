import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post



def post_list(request):

    # 경로에 해당하는 HTMl파일을 문자열로 로드해줌
    result = '글 목록<br>'
    posts = Post.objects.all()
    for post in posts:
        result += '-{}<br>'.format(post.title)

    return HttpResponse(result)





