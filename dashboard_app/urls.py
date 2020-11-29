from django.urls import path
from dashboard_app.views import *
urlpatterns = [
    path('', home, name='home'),
    path('credit/<slug:slug>/',credit,name='credit')
]