from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('aksesoris/', include('aksesoris.urls')),
    path('casing/', include('casing.urls')),
    path('hp/', include('hp.urls')),
]
