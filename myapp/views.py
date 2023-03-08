from django.shortcuts import render, redirect
from django.contrib import messages
from myapp import models
import pymysql
import tkinter.messagebox
from tkinter import *

# 网站默认界面
def index(request):
    context_dict = {}
    context_dict['boldmessage'] = '网站默认界面，限制酒厂的信息和两种登陆方法的链接！'

    return render(request, 'myapp/index.html', context=context_dict)

# 经理登陆
def manager_login(request):
    if request.method == 'POST':
        manager_name = request.POST.get('manager_name')
        manager_password = request.POST.get('manager_password')

        if manager_name and manager_password:
            name = manager_name.strip()
            try:
                manager = models.Manager.objects.get(manager_name=name)
            except:
                return render(request, 'myapp/index.html')
            if manager.manager_pw == manager_password:
                return redirect('myapp:manager_home')

    return render(request, 'myapp/manager_login.html')

# admin登陆
def administrator_login(request):
    if request.method == 'POST':
        administrator_name = request.POST.get('administrator_name')
        administrator_password = request.POST.get('administrator_password')

        if administrator_name and administrator_password:
            name = administrator_name.strip()
            try:
                administrator = models.Administrator.objects.get(admin_name=name)
            except:
                return render(request, 'myapp/index.html')
            if administrator.admin_pw == administrator_password:
                return redirect('myapp:administrator_home')

    return render(request, 'myapp/administrator_login.html')

# 经理主界面，直接显示所用admin的信息
def manager_home(request):
    context_dict = {}
    conn = pymysql.connect(host='localhost', user='root', password='12345678', db='drinks', charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT admin_id,admin_name,admin_pw,admin_age,admin_email,admin_telephone FROM administrator')
        administrators = cursor.fetchall()
    context_dict['administrators'] = administrators
    return render(request, 'myapp/manager_home.html', context_dict)

# 添加admin账户
def add_admin(request):
    if request.method == 'GET':
        return render(request, 'myapp/add_admin.html')
    else:
        admin_name = request.POST.get('admin_name', '')
        admin_pw = request.POST.get('admin_pw', '')
        manager_name = request.POST.get('manager_name')
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO administrator (admin_name,admin_pw,manager_name)"
                           "values (%s,%s,%s)", [admin_name,admin_pw,manager_name])
            conn.commit()
    return redirect('../')

# 修改admin账户
def edit_admin(request):
    if request.method == 'GET':
        admin_id = request.GET.get('admin_id')
        context_dict = {}
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT admin_id,admin_name,admin_pw FROM administrator where admin_id =%s", [admin_id])
            admin = cursor.fetchone()
        context_dict['administrator'] = admin
        return render(request, 'myapp/edit_admin.html', context_dict)
    else:
        admin_id = request.POST.get('admin_id')
        admin_name = request.POST.get("admin_name")
        admin_pw = request.POST.get('admin_pw', '')
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE administrator SET admin_name=%s,admin_pw=%s where admin_id =%s",
                           [admin_name, admin_pw, admin_id])
            conn.commit()
        return redirect('../')

def delete_admin(request):
    admin_id = request.GET.get('admin_id')
    conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM administrator WHERE admin_id=%s",[admin_id])
        conn.commit()
    return redirect('../')

# admin主界面
def administrator_home(request):
    return render(request, 'myapp/administrator_home.html')

def personal_information(request):
    return render(request, 'myapp/personal_information.html')

def warehouse(request):
    return render(request, 'myapp/warehouse.html')

def record(request):
    return render(request, 'myapp/record.html')