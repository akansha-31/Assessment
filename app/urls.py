from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors', views.get_top_contributors, name='contributors'),
    path('commits', views.get_all_commits, name='commits'),
    path('starred', views.get_starred_repos, name='starred_repo'),
    path('mail', views.send_mail, name='send_mail'),
]
