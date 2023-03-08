from myapp import views
from django.urls import path,re_path

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('administrator_home/', views.administrator_home, name='administrator_home'),
    path('manager_home/', views.manager_home, name='manager_home'),
    path('personal_information/', views.personal_information, name='personal_information'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('record/', views.record, name='record'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('edit_admin/', views.edit_admin, name='edit_admin'),
    path('delete_admin/', views.delete_admin, name='delete_admin'),
]
