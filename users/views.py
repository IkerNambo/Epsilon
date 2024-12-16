from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import UserForm
import time
from django.contrib.auth import authenticate, login, logout
from .mail import RegisterMail
# Create your views here.



def RegisterView(request,*args,**kwargs):
    form = UserForm()
    try:
      if request.method == 'POST':
          form = UserForm(request.POST)
          if form.is_valid:
              form.save()
              return redirect('/users/Login')
      else:
          UserForm() 
    except ValueError:
        registermessage = messages.success(request, "registration failed, check the information and try again")
    authuser = request.user.is_authenticated

  
    context = {
        'form': form,
        'auuser': authuser
    }
    return render(request, 'users/Registerview.html', context)


def LoginView(request, *ruby, **rose):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=username,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('EmptyView')
         
        else:
            loginmessage = messages.success(request, 'Information is incorrect')
    return render(request, 'users/Loginview.html' )


def UserManageView(request, *blake, **belladona):
    if request.user.is_authenticated == True:
      username = request.user
      email = request.user.email
      
      context = {
          'username': username,
          'email': email
      }
      return render(request, 'configuration/Usermanageview.html', context)
    else:
        return redirect('EmptyView')
  