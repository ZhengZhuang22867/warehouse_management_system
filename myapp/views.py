from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp import models

# Create your views here.
def index(request):
    context_dict = {}
    context_dict['boldmessage'] = '网站默认界面，限制酒厂的信息和两种登陆方法的链接！'

    return render(request, 'myapp/index.html', context=context_dict)

def manager_login(request):
    if request.method == 'POST':
        manager_name = request.POST.get('manager_name')
        manager_password = request.POST.get('manager_password')

        # if administrator_name == 'zheng' and administrator_password == '123456':
        #     return redirect('myapp:administrator_home')
        # else:
        #     return render(request, 'myapp/index.html')

        if manager_name and manager_password:
            name = manager_name.strip()
            try:
                manager = models.Manager.objects.get(manager_name=name)
            except:
                return render(request, 'myapp/index.html')
            if manager.manager_pw == manager_password:
                return redirect('myapp:manager_home')

    return render(request, 'myapp/manager_login.html')

def administrator_login(request):
    if request.method == 'POST':
        administrator_name = request.POST.get('administrator_name')
        administrator_password = request.POST.get('administrator_password')

        # if administrator_name == 'zheng' and administrator_password == '123456':
        #     return redirect('myapp:administrator_home')
        # else:
        #     return render(request, 'myapp/index.html')

        if administrator_name and administrator_password:
            name = administrator_name.strip()
            try:
                administrator = models.Administrator.objects.get(admin_name=name)
            except:
                return render(request, 'myapp/index.html')
            if administrator.admin_pw == administrator_password:
                return redirect('myapp:administrator_home')

    return render(request, 'myapp/administrator_login.html')

def manager_home(request):
    return HttpResponse('manager home')

def administrator_home(request):
    return HttpResponse('administrator home')
