from django.shortcuts import HttpResponse
import csv
import json 
from app.views import get_all_repos

def get_all_commits(request):
    all_commits = []
    repos = get_all_repos(request)
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
    json_data['all_commits'] = all_commits
    with open("data.json", "w") as outfile:
        json.dump(json_data, outfile, default=str, indent=4)
    return HttpResponse("commit")
