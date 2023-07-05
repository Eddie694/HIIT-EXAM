from django.urls import path
from .import views

app_name ='examform'

urlpatterns = [
    path('', views.home, name = 'form'),
]
