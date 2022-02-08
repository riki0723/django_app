from django.shortcuts import render
from django.http import HttpResponse
# HttpResponseというクラスをimportする。


def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'hello/index.html',params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう1つのページです。',
        'goto':'index',
    }
    return render(request, 'hello/index.html',params)

#importされたクラスを実行する処理の内容
#def index(request): index関数を定義しますよという意味
#return HttpResponse〜で実行内容
#
# Create your views here.
