from celery import shared_task
from django.template.loader import get_template
from django.conf import settings

from news_app.utils import send_email
from fetch_news.models import Article


@shared_task
def notify_user(user_email, article_list):
    articles = Article.objects.filter(
        id__in=article_list
    ).values('id', 'title')
    if articles:
        context = {'articles': articles, 'site_url': settings.SITE_URL}
        html_content = get_template(
            'mail_templates/notify_news.html'
        ).render(context)
        send_email("Notfication", user_email, html_content=html_content)
    return True
