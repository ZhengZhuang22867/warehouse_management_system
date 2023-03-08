from myapp import views
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('administrator_home/', views.administrator_home, name='administrator_home'),
    path('manager_home/', views.manager_home, name='manager_home'),
]