import pandas as pd
from github import Github
from django.http import HttpResponse
import json

def get_starred_repos(request):
    df = pd.read_csv('contributors.csv')
    github = Github('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')
    starred_repos = {}
    for user in df['username']:
        user_obj = github.get_user(user)
        repos = user_obj.get_starred()
        starred_repo = [repo.full_name for repo in repos]
        starred_repos[user]= starred_repo
    with open("starred.json", "w") as outfile:
        json.dump(starred_repos, outfile, default=str, indent=4)
    return HttpResponse("starred repos")