from django.urls import path
from profile_app.views import *
urlpatterns = [
    path('<str:username>/',profile_views,name='profile_links')
]