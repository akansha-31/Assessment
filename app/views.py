from django.shortcuts import render, HttpResponse, redirect
from app.forms import ValideGitUrl
import re
import csv
import json 
from urllib.parse import urlparse
from github import Github
from datetime import datetime
import pandas as pd

def validate(request):
    form = ValideGitUrl()
    if request.method == 'POST':
        regex = r'^(http(s?):\/\/)?(www\.)?github\.com\/([A-Za-z0-9\-]{1,})+\/?$'
        url = request.POST['url']
        request.session['organization'] = urlparse(url).path[1:]
        if bool(re.match(regex,url)):
            return redirect(get_all_commits)
        else:
            return HttpResponse("Invalid git url")
    elif request.method == 'GET':
        return render(request,'index.html', {'form': form})

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

def get_all_repos(request):
    github = Github('akansha-31', 'Siroliya@123')
    organization = github.get_organization('coindcx-official')

    repos = []
    for repo in organization.get_repos():
        repos.append(repo)
    return repos

def get_top_contributors(request):
    df = pd.read_csv('all_commits.csv')
    top_contributors = dataframe['committer'].value_counts().nlargest(10).reset_index()
    top_contributors.columns = ['author', 'commit_count']
    top_contributors.to_csv('contributors.csv', index=False)