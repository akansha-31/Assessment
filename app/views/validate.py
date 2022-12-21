from django.shortcuts import render, HttpResponse, redirect
from app.forms import ValideGitUrl
import re
from app.views import get_all_commits
from urllib.parse import urlparse

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
