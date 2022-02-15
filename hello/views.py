from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
# HttpResponseというクラスをimportする。


def index(request):
    params = {
        'title':'Hello',
        'msg':'your data:',
        'form': HelloForm()
    }
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + '<br>メール：' + request.POST['mail'] + '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html',params)

#importされたクラスを実行する処理の内容
#def index(request): index関数を定義しますよという意味
#return HttpResponse〜で実行内容
#
# Create your views here.
