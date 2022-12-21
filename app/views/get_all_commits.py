from django.shortcuts import HttpResponse
import csv
from github import Github
import json 
from app.views import get_all_repos

def get_all_commits(request):
    all_commits = []
    repos = get_all_repos()
    column_names = ['committer', 'timestamp']

    with open("all_commits.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()

        for repo in repos:
            for commit in repo.get_commits():
                commits = {}
                commits['committer'] = commit.commit.author.name
                commits['timestamp'] = commit.commit.committer.date
                writer.writerow(commits)
                all_commits.append(commits)

    sorted_commits = sorted(all_commits,key=lambda x: x['timestamp'], reverse=True)[:500]
    json_data = {}
    json_data['all_commits'] = sorted_commits
    with open("data.json", "w") as outfile:
        json.dump(json_data, outfile, default=str, indent=4)
    return HttpResponse("commit")


def get_all_repos():
    github = Github('akansha-31', 'Siroliya@123')
    organization = github.get_organization('coindcx-official')

    repos = []
    for repo in organization.get_repos():
        repos.append(repo)
    return repos
