from django.core.mail import EmailMultiAlternatives
from django.utils.crypto import get_random_string
# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])


def send_email( email):
    token = get_random_string(length=32)
    # request.user.verify_token = token
    # request.user.save()

    verify_link = path + 'email-verify/' + token
    subject, from_email, to = 'Verify Your Email', 'from@test.com', email
    html_content = render_to_string('verify_email.html', {'verify_link':verify_link, 'base_url': path, 'backend_url': path}) 
    text_content = strip_tags(html_content) 

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()