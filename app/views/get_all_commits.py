from django.shortcuts import HttpResponse
import csv
from github import Github
import json 

def get_all_commits(request):
    all_commits = []
    repos = get_all_repos(request)
    column_names = ['username','committer', 'timestamp']

    with open("all_commits.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()

        for repo in repos:
            for commit in repo.get_commits():
                commits = {}
                if commit.author == None:
                    continue
                else:
                    commits['username'] = commit.author.login
                    commits['committer'] = commit.commit.author.name
                    commits['timestamp'] = commit.commit.committer.date
                    writer.writerow(commits)
                    all_commits.append(commits)

    sorted_commits = sorted(all_commits,key=lambda x: x['timestamp'], reverse=True)[:500]
    json_data = {}
    json_data['all_commits'] = sorted_commits
    with open("data.json", "w") as outfile:
        json.dump(json_data, outfile, default=str, indent=4)
    return HttpResponse(sorted_commits)


def get_all_repos(request):
    github = Github('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')
    organization = github.get_organization(request.session['organization'])

    repos = []
    for repo in organization.get_repos():
        repos.append(repo)
    return repos
