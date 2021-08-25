from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.utils.tokens import account_activation_token

def send_confirmation_email(user, site_adress):
    context = {
        'site_adress': site_adress,
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    html_message = render_to_string('emails/account_activation_email.html', context=context)
    subject = "Please verify your email for [SuperB]"
    email = EmailMessage(subject=subject, body=html_message, from_email=settings.EMAIL_HOST_USER, to=[user.email])
    email.content_subtype = "html"
    email.send()