from .base import *
import environ

env = environ.Env()
environ.Env.read_env()


DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = [".herpkuapp.com", ".elasticbeanstalk.com"]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]