
from django.contrib import admin
from django.urls import path,include    
from .views import *
urlpatterns = [
    path('', test , name = 'test'),
    path('sendmail/', send_mail_to_all, name = 'sendmail'),
  
]
