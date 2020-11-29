from django.urls import path
from user_app.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('otp/<str:phone_number>/', otp_views, name='otp'),
]