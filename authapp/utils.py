from django.urls import reverse
from django.core.mail import send_mail

from shop import settings


def send_verify_email(user):
    verify_link = settings.DOMAIN_NAME + reverse('auth:verify', args=[user.id, user.activation_key])
    subject = f'Подтвердите регистрацию {user.email}'
    message = f'Для активации аккаунта перейдите по ссылке: \n {verify_link}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    return send_mail(subject, message, email_from, recipient_list, fail_silently=False)