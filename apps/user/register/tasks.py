
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import mail

from configs.celery import app


@app.task()
def send_activation_mail(user_email, activate_token):
    connection = mail.get_connection(
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS,
        use_ssl=settings.EMAIL_USE_SSL
    )

    email_message = (
        f"""<br><b>Please follow the link to activate your account:</b> <br/><br/>
        {settings.DOMAIN}api/v1/user_activate/{activate_token}/'"""
    )

    msg = EmailMessage(
        subject="Account Activation",
        body=email_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email],
        connection=connection
    )
    msg.content_subtype = "html"
    if msg.send():
        print("Sent")
    else:
        print("Not sent")
