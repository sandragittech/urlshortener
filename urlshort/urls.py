
from django.urls import path, include
from .views import home, createShortURL, redirect
urlpatterns = [
   path('',home, name='home'),
   path('create/', createShortURL, name='create'),
   path('<str:url>', redirect, name='redirect')
]