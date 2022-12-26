from django.http import HttpResponse
from django.core.mail import EmailMessage


    

def send_mail(request):
    mail = EmailMessage('Files', '', 'akansharma31@gmail.com', ['akansharma31@gmail.com'])
    mail.attach_file('/Users/akansha/Desktop/Home/Training/Assessment/project/contributors.csv')
    mail.attach_file('/Users/akansha/Desktop/Home/Training/Assessment/project/all_commits.csv')
    mail.attach_file('/Users/akansha/Desktop/Home/Training/Assessment/project/data.json')
    mail.send()
    return HttpResponse("sent")