from django.shortcuts import render, HttpResponse
from app.forms import ValideGitUrl
import re
from urllib.parse import urlparse

def index(request):
    form = ValideGitUrl()
    if request.method == 'POST':
        regex = r'^(http(s?):\/\/)?(www\.)?github\.com\/([A-Za-z0-9\-]{1,})+\/?$'
        url = request.POST['url']
        request.session['organization'] = urlparse(url).path[1:]
        if bool(re.match(regex,url)):
            return render(request, 'dashboard.html')
        else:
            return HttpResponse("Invalid git url")
    elif request.method == 'GET':
        return render(request,'index.html', {'form': form})
