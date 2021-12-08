from django.shortcuts import render
from django.http import HttpResponse
# HttpResponseというクラスをimportする。


def index(request,id,nickname):
    result = 'your id: ' + str(id) + ', name:"' + nickname + '".'
    return HttpResponse(result)
#importされたクラスを実行する処理の内容
#def index(request): index関数を定義しますよという意味
#return HttpResponse〜で実行内容
#
# Create your views here.
