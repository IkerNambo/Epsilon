from django.shortcuts import render
from django.http import HttpResponse
from users.models import SiteUsers 
# Create your views here.


def EmptyView(request, *args, **kwargs):
    user = request.user
    authuser = request.user.is_authenticated
    context = {
        'user': user,
        'auuser': authuser
    }
    return render(request, 'home.html', context)