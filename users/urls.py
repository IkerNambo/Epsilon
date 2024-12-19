from django.urls import path, include

from . import views

urlpatterns = [
    path('Register/', views.RegisterView, name='RegisterView'),
    path('Login/' , views.LoginView, name='Login'),
    path('Settings/', views.UserManageView, name='Settings'),
    path('Settings/UsernameReset/', views.UsernameChangeView, name='UsernameReset'),
    path('Settings/EmailReset/', views.EmailChangeView, name='EmailReset'),
    path('Settings/PasswordReset/', views.PasswordChangeView, name='PasswordReset'),
]
