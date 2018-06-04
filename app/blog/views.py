import os
from django.http import HttpResponse
from django.template.loader import render_to_string


def post_list(request):

    # 경로에 해당하는 HTMl파일을 문자열로 로드해줌
    html = render_to_string('blog/post_list.html')
    return HttpResponse(html)
