# comments/urls.py
from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),               # List all comments
    path('add/', views.add_comment, name='add_comment'),             # Add a new comment
    path('<int:pk>/edit/', views.edit_comment, name='edit_comment'), # Edit a specific comment
    path('<int:pk>/delete/', views.delete_comment, name='delete_comment'), # Delete a specific comment
]
