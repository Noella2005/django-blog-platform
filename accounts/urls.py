from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.account_home, name='account_home'),
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
]
