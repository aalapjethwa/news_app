FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /newsapp
COPY requirements.txt /newsapp/

COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

RUN pip install -r requirements.txt
COPY . /newsapp/
