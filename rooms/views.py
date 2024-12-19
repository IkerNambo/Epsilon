from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
import time
from django.contrib.auth import authenticate, login, logout
from users.mail import RegisterMail

def LobbyView(request, *blake,**belladona):
    if request.user.is_authenticated == True:
        return render(request, 'chat/lobbyview.html', {})
    else:
        return redirect('RegisterView')
# Create your views here.
