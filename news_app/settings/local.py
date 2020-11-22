from .base import *
from .base import env


DEBUG = env("DEBUG", default=True)
# PostgreSQL database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': 5432,
    }
}


SITE_URL = "http://localhost:8000"
ALLOWED_HOSTS = ['*']
