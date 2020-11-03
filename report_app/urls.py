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
    path('payroll/', views.payroll, name='payroll'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('change_password/',views.change_password,name='password_change'),
]
