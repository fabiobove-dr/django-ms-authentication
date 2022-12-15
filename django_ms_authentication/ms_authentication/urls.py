
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('home', views.login, name='home'),   
    path('login', views.login, name='login'),  
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
]