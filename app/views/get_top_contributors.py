from django.shortcuts import render, HttpResponse, redirect
from app.forms import ValideGitUrl
import re
import csv
import json 
from urllib.parse import urlparse
from github import Github
from datetime import datetime
import pandas as pd


def get_top_contributors(request):
    df = pd.read_csv('all_commits.csv')
    top_contributors = dataframe['committer'].value_counts().nlargest(10).reset_index()
    top_contributors.columns = ['author', 'commit_count']
    top_contributors.to_csv('contributors.csv', index=False)