from django.urls import path
from app import views

urlpatterns = [
    path('', views.validate, name='validate'),
    path('commits', views.get_all_commits, name='commits'),
]
