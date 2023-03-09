from django.shortcuts import render, redirect
from django.contrib import messages
from myapp import models
import pymysql
import tkinter.messagebox
from tkinter import *

# 网站默认界面
def index(request):
    context_dict = {}
    context_dict['boldmessage'] = '网站默认界面，显示酒厂的信息和两种登陆方法的链接！'
    return render(request, 'myapp/index.html', context=context_dict)

# 经理登录
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

# admin登录
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
                request.session['admin_id'] = administrator.admin_id
                return render(request, 'myapp/administrator_home.html')

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
    return render(request, 'myapp/manager_login.html')

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
        return render(request, 'myapp/manager_login.html')

def delete_admin(request):
    admin_id = request.GET.get('admin_id')
    conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM administrator WHERE admin_id=%s",[admin_id])
        conn.commit()
    return render(request, 'myapp/manager_login.html')

# admin主界面
def administrator_home(request):
    return render(request, 'myapp/administrator_home.html')

def profile_information(request):
    admin_id = request.session.get('admin_id')
    context_dict = {}
    conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT admin_id,admin_name,admin_pw,admin_age,admin_email,admin_telephone FROM administrator where admin_id =%s", [admin_id])
        admin = cursor.fetchone()
    context_dict['administrator'] = admin
    return render(request, 'myapp/profile_information.html', context_dict)

def edit_profile(request):
    if request.method == 'GET':
        admin_id = request.GET.get('admin_id')
        context_dict = {}
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT admin_id,admin_name,admin_pw,admin_age, admin_email, admin_telephone FROM administrator where admin_id =%s", [admin_id])
            admin = cursor.fetchone()
        context_dict['administrator'] = admin
        return render(request, 'myapp/edit_profile.html', context_dict)
    else:
        admin_id = request.POST.get('admin_id')
        admin_name = request.POST.get("admin_name")
        admin_pw = request.POST.get('admin_pw', '')
        admin_age = request.POST.get('admin_age')
        admin_email = request.POST.get('admin_email')
        admin_telephone = request.POST.get('admin_telephone')
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE administrator SET admin_name=%s,admin_pw=%s,admin_age=%s,admin_email=%s,admin_telephone=%s where admin_id =%s",
                           [admin_name, admin_pw, admin_age, admin_email, admin_telephone, admin_id])
            conn.commit()
        return render(request, 'myapp/administrator_login.html')

def warehouse(request):
    admin_id = request.session.get('admin_id')
    warehouse = models.Warehouse.objects.get(admin_id=admin_id)
    warehouse_id = warehouse.warehouse_id
    context_dict = {}
    conn = pymysql.connect(host='localhost', user='root', password='12345678', db='drinks', charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT product_id,name,type,number FROM product WHERE warehouse_id=%s',
                       [warehouse_id])
        products = cursor.fetchall()
    context_dict['products'] = products
    context_dict['warehouse_id'] = warehouse_id
    return render(request, 'myapp/warehouse.html', context_dict)

def check_product(request):
    product_id = request.GET.get('product_id')
    context_dict = {}
    conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute(
            'SELECT product_id,name,type,purchase_price,selling_price,number,supplier FROM product WHERE product_id=%s',
                       [product_id]
        )
        product = cursor.fetchone()
    context_dict['product'] = product
    return render(request, 'myapp/check_product.html',context_dict)

def add_product(request):
    if request.method == 'GET':
        return render(request, 'myapp/add_product.html')
    else:
        warehouse_id = request.POST.get('warehouse_id', '')
        name = request.POST.get('name','')
        type = request.POST.get('type','')
        purchase_price = request.POST.get('purchase_price', '')
        selling_price = request.POST.get('selling_price', '')
        number = request.POST.get('number', '')
        supplier = request.POST.get('supplier', '')
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "INSERT INTO product (warehouse_id,name,type,purchase_price,selling_price,number,supplier)"
                           "values (%s,%s,%s,%s,%s,%s,%s)", [warehouse_id,name,type,purchase_price,selling_price,number,supplier])
            conn.commit()
        product_new = models.Product.objects.get(name = name, type = type, warehouse_id=warehouse_id, number = number)
        product_id = product_new.product_id
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "INSERT INTO record (product_id,warehouse_id,number) values (%s,%s,%s)",
                [product_id,warehouse_id,number])
            conn.commit()
    return render(request, 'myapp/administrator_login.html')

def edit_product(request):
        if request.method == 'GET':
            product_id = request.GET.get('product_id')
            global number_old
            global warehouse_id_temp
            product = models.Product.objects.get(product_id = product_id)
            number_old = int(product.number)
            warehouse_id_temp = product.warehouse_id
            context_dict = {}
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
            with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT product_id,warehouse_id,name,type,purchase_price,"
                               "selling_price,number,supplier FROM product where product_id =%s", [product_id])
                product = cursor.fetchone()
            context_dict['product'] = product
            return render(request, 'myapp/edit_product.html', context_dict)
        else:
            product_id = request.POST.get('product_id')
            name = request.POST.get('name','')
            type = request.POST.get("type",'')
            purchase_price = request.POST.get('purchase_price', '')
            selling_price = request.POST.get('selling_price','')
            number = request.POST.get('number','')
            supplier = request.POST.get('supplier','')
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="drinks", charset='utf8')
            with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                cursor.execute("UPDATE product SET name=%s,type=%s,purchase_price=%s,"
                               "selling_price=%s,number=%s,supplier=%s where product_id =%s",
                               [name, type, purchase_price, selling_price, number, supplier,product_id])
                conn.commit()
            number_new = int(number) - number_old
            number_new = str(number_new)
            with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO record (product_id,warehouse_id,number) values (%s,%s,%s)",
                    [product_id, warehouse_id_temp, number_new])
                conn.commit()
            return render(request, 'myapp/administrator_login.html')

def record(request):
    admin_id = request.session.get('admin_id')
    warehouse = models.Warehouse.objects.get(admin_id=admin_id)
    warehouse_id = warehouse.warehouse_id
    context_dict = {}
    conn = pymysql.connect(host='localhost', user='root', password='12345678', db='drinks', charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT product_id,warehouse_id,number FROM record WHERE warehouse_id=%s',
                       [warehouse_id])
        records = cursor.fetchall()
    context_dict['records'] = records
    context_dict['warehouse_id'] = warehouse_id
    return render(request, 'myapp/record.html', context_dict)
