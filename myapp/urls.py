from myapp import views
from django.urls import path,re_path

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('administrator_home/', views.administrator_home, name='administrator_home'),
    path('manager_home/', views.manager_home, name='manager_home'),
    path('profile_information/', views.profile_information, name='profile_information'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('record/', views.record, name='record'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('edit_admin/', views.edit_admin, name='edit_admin'),
    path('delete_admin/', views.delete_admin, name='delete_admin'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('check_product/', views.check_product, name='check_product'),
    path('add_product/', views.add_product, name='add_product'),
]
