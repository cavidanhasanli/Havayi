from django.shortcuts import render, HttpResponse
from profile_app.models import *
from user_app.models import *

# Create your views here.

def profile_views(request, username):
    context = {'title': 'Şəxsi kabinet'}
    context['user_cash'] = MyUser.objects.filter(username=username)
    return render(request, 'profile.html', context)
