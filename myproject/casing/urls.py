from django.urls import path
from . import views
app_name = 'casing'

urlpatterns = [
    path('', views.index),
]