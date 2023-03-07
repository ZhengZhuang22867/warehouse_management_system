from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
]