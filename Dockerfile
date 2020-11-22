FROM python:3.8
WORKDIR /newsapp
COPY requirements.txt /newsapp/

COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./compose/celery/start /start-celery
RUN sed -i 's/\r//' /start-celery
RUN chmod +x /start-celery

COPY ./compose/celerybeat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

RUN pip install -r requirements.txt
COPY . /newsapp/
