from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import UserForm, ChangeEmailForm, ChangePasswordForm
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
        messages.error(request, "Registration failed, check the information and try again")
    authuser = request.user.is_authenticated

  
    context = {
        'form': form,
        'auuser': authuser
    }
    return render(request, 'users/Registerview.html', context)


def LoginView(request, *ruby, **rose):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('EmptyView')
         
        else:
            messages.error(request, 'Information is incorrect')
    return render(request, 'users/Loginview.html' )

# this section is dedicated entirely to the settings tab of the website

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

def UsernameChangeView(request, *args, **kwargs):
    
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            newusername = request.POST.get('username')
            print(newusername)
            user = request.user
            userlength = len(newusername)
            
            if newusername != '' and newusername is not None and userlength <= 20:
              user.username = newusername  
              user.save()
              
              return redirect('Settings')
            else:
                messages.error(request, 'Please enter a valid name')
      
        return render(request, 'configuration/usernamereset.html', {})
    else:
        return redirect('EmptyView')

def EmailChangeView(request, *args, **kwargs):
    if request.user.is_authenticated == True:
        form = ChangeEmailForm()
        
        if request.method == 'POST':
          form = ChangeEmailForm(request.POST, instance=request.user)
          
          if form.is_valid():
              form.save()
              return redirect('Settings')
      
        context = {
            'form': form
        }
        return render(request, 'configuration/emailreset.html', context)
    else:
      return redirect('EmptyView')

def PasswordChangeView(request, *args, **kwargs):
    if request.user.is_authenticated == True:
        form = ChangePasswordForm(User)
        
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
        
        context = {
            'form': form
        }
                
        return render(request, 'configuration/passwordchange.html', context)
    else:
      return redirect('EmptyView')

def DeleteAccountView(request, *args, **kwargs):
    if request.user.is_authenticated == True:
        user = request.user
           
        if request.method == 'POST':
            deleteform = request.POST.get('deleteuser')
            uid = request.user.id
            
            
            if deleteform == 'CONFIRM':
                print('Done done done.. aaaaaand done')
                user.delete()
                return redirect('EmptyView')
              
            else:
                messages.error(request, "Failed, You didn't type CONFIRM in all caps.")
                print(uid)
                print('failed')
                print(deleteform)
            
            
        return render(request, 'configuration/accountdelete.html')
    
    else:
        return redirect('EmptyView')
  