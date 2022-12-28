from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('aksesoris/', include('aksesoris.urls',namespace='aksesoris')),
    path('casing/', include('casing.urls',namespace='casing')),
    path('hp/', include('hp.urls',namespace='hp')),
]
