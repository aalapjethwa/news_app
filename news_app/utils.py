from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings


def send_email(
    subject, recepient, text_content="", html_content=""
):
    ''' Generic mail sending function for prepending tags. '''
    if type(recepient) == str:
        recepient = [recepient]
    subject = "NewsApp: " + subject
    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=recepient,
        )
        if html_content:
            msg.attach_alternative(html_content, "text/html")
        msg.send()
        print(f"Sent mail to: {recepient}")
    except Exception as e:
        print(e)
        print(f"Mail sending failed for users: {recepient}")
    return True
