from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def send_email_view(request):
    subject = 'Hello from Django'
    message = 'This is a test email from Django.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['fazeejalb@gmail.com']
    
    # Send the email
    send_mail(subject, message, email_from, recipient_list)

    # Return an HttpResponse to indicate success
    return HttpResponse("Email sent successfully!")

    
