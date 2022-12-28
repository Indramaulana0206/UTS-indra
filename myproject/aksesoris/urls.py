from django.urls import path
from . import views
app_name = 'aksesoris'

urlpatterns = [
    path('', views.index)
]