from django.shortcuts import render, HttpResponse
from profile_app.models import *


# Create your views here.

def profile_views(request, username):
    context = {'title': 'Şəxsi kabinet'}
    return render(request, 'profile.html', context)
