from django.contrib.auth import views as dara_auth_views
from django.urls import path

from . import views
from .forms import LogInForm


app_name = 'core' # used in HTML file for calling def in core/views.py

urlpatterns = [
    path('', views.index, name='index'), 
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', dara_auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LogInForm), name='login'),
]