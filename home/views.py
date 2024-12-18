from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def EmptyView(request, *args, **kwargs):
    user = request.user
    authuser = request.user.is_authenticated
    context = {
        'user': user,
        'auuser': authuser
    }
    return render(request, 'home.html', context)

def AboutView(request, *golden, **ray):
    return render(request, 'about.html', {})