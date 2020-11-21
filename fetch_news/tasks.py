from celery.task import periodic_task
from celery.schedules import crontab


@periodic_task(run_every=crontab(minute="*/1"))
def hearbeat():
    print("Working....")
