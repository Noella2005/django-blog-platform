from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts_home'),
]
