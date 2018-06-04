import os
from django.http import HttpResponse
from django.shortcuts import render



def post_list(request):

    # 경로에 해당하는 HTMl파일을 문자열로 로드해줌
    return render(request, 'blog/post_list.html')

