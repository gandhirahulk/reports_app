from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from report_app import views

app_name = 'report_app'

urlpatterns = [
    path('', views.csp_login, name='login'),
    path('logout/', views.csp_logout, name='csp_logout'),
    path('notlogin/', views.notlogin, name='notlogin'),
    path('payroll/', views.payroll, name='payroll')]
