import os

from celery import Celery
from django.conf import settings
from django.apps import apps, AppConfig


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app.settings')

app = Celery('news_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


class CeleryAppConfig(AppConfig):
    name = "taskapp"
    verbose_name = "Celery Config"

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
