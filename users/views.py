from django.shortcuts import render
from .forms import UserForm
from .models import SiteUsers
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.



def LoginView(request,*args,**kwargs):
    form = UserForm()
    authuser = request.user.is_authenticated
  
    userrq = request.user
    try:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                SiteUsers.objects.create(**form.cleaned_data)
                form = UserForm()
    except IntegrityError:
        messages.error(request, 'Email is already in use.')
        print(f'{userrq}  did samey')
    context = {
        'form': form,
        'auuser': authuser
    }
    return render(request, 'users/Loginview.html', context)