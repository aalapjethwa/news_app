from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import AppUser
from fetch_news.models import Article, TaskQueue, Category
from users.tasks import notify_user


@receiver(post_save, sender=TaskQueue)
def prepare_user_notification(sender, instance, **kwargs):
    try:
        if instance.is_finished:
            return
        categories = Category.objects.filter(articles__bulk_ref=instance.bulk_ref).distinct()
        for cat in categories:
            notify_user(cat.user_emails, cat.article_list, cat.name)
        instance.is_finished=True
        instance.save()
    except Exception as e:
        print(f"Exception occured in signals: {e}")
    return
