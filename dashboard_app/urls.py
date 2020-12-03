from django.urls import path
from dashboard_app.views import *
urlpatterns = [
    path('', credit_page, name='credit_page'),
    path('credit/<slug:slug>/',credit,name='credit'),
    path('otp/<str:phone_number>/', otp_views, name='otp_code'),
]