from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors', views.get_top_contributors, name='contributors'),
    path('commits', views.get_all_commits, name='commits'),
]
