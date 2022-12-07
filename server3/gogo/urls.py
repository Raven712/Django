from django.urls import path
from . import views

app_name = 'gogo'

urlpatterns = [
    path('', views.gogo),
]