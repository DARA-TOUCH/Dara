from django.urls import path

from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.list01, name='list01'),
]