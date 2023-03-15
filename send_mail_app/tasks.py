from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from celery import shared_task
from djangoceleryproject import settings

@shared_task(bind = True)
def send_mail_func(request):
    user = get_user_model().objects.all()
    for user in user:
        mail_subject = 'Activate your account.'
        message = 'If is celery working, please click on the link below to activate your account.'
        to_email = user.email
        print("to_email",to_email)
        send_mail(
            subject= mail_subject,
            message= message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list= [to_email],
            fail_silently= True,
        )
    return "Done send mail"