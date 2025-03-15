from django.contrib import admin
from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('auth/', auth, name='auth'),
]
