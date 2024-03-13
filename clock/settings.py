
import os 
from clock import setting

SECRET_KEY = os.environ.get('SECRETE_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
INSTALLED_APPS = setting.INSTALLED_APPS
MIDDLEWARE = setting.MIDDLEWARE
WSGI_APPLICATION = "clock.wsgi.application"
DATABASES = setting.DATABASES
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
ROOT_URLCONF = "clock.urls"
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TEMPLATES = setting.TEMPLATES

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]
