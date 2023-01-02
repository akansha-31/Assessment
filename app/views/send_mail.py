from django.http import HttpResponse
from django.core.mail import EmailMessage
from pathlib import Path
from os.path import join
    

def send_mail(request):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    
    mail = EmailMessage('Files', '', 'akansharma31@gmail.com', ['akansharma31@gmail.com'])
    mail.attach_file(join(BASE_DIR, 'contributors.csv'))
    mail.attach_file(join(BASE_DIR, 'all_commits.csv'))
    mail.attach_file(join(BASE_DIR, 'data.json'))
    mail.send()
    return HttpResponse("sent")