from django.core.mail import send_mail
from django.conf import settings

def send_new_blog_email(news):
    subject = 'Novo blog criado: ' + news.title
    message = 'Um novo blog foi criado: ' + news.title + '\n\n' + news.body
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['team@example.com']
    send_mail(subject, message, email_from, recipient_list)
