from django.shortcuts import render
from django.http import HttpResponse
from login.models import Manager

# Create your views here.
def index(request):
    context_dict = {}
    context_dict['boldmessage'] = '网站的默认界面，这里要展示酒厂信息！还有manager和admin的登陆界面的链接！'
    return render(request, 'login/index.html', context_dict)

def manager_login(request):
    a = Manager.objects.all().values('manager_name')
    print(a)
    return HttpResponse("在这个界面实现manager的登陆！")

def administrator_login(request):
    return HttpResponse("在这个界面实现administrator的登陆！")