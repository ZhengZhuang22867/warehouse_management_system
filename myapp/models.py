from django.db import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# from login.models import Manager

class Administrator(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    manager_name = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_name')
    admin_name = models.CharField(max_length=255, blank=True, null=True)
    admin_pw = models.CharField(max_length=255)
    admin_age = models.IntegerField(blank=True, null=True)
    admin_email = models.CharField(max_length=255, blank=True, null=True)
    admin_telephone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'administrator'

class Manager(models.Model):
    manager_name = models.CharField(primary_key=True, max_length=255)
    manager_pw = models.CharField(max_length=255)
    manager_age = models.IntegerField(blank=True, null=True)
    manager_email = models.CharField(max_length=255, blank=True, null=True)
    manager_telephone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manager'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product'


class Record(models.Model):
    record_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    warehouse_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'record'


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)
    admin = models.ForeignKey(Administrator, models.DO_NOTHING)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'warehouse'

class AdminProfile(models.Model):
    admin = models.OneToOneField(Administrator, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='default.jpg', blank=True)

    def __str__(self):
        return self.admin.admin_name


