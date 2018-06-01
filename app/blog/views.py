import os
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):

    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    app_dir = os.path.dirname(dir_name)
    tem_dir = os.path.join(app_dir,'templates')
    tem_blog = os.path.join(tem_dir, 'blog', 'post_list.html')
    html = open(tem_blog, 'rt').read()
    return HttpResponse(
        html
    )

    # return HttpResponse(
    #     '<html>'
    #     '<body>'
    #     '   <h1>Post List<h1>'
    #     '   <p>Post list page</p>'
    #     '   <img src="https://t1.daumcdn.net/cfile/tistory/22334E4F5900DDE029"'
    #     '</body>'
    #     '</html>')
