"""
Django settings for www_ReDesignIT_pl project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from os import getenv
from dotenv import load_dotenv
from easy_thumbnails.conf import Settings as thumbnail_settings

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['159.223.30.131', 'redesignit.pl', 'www.redesignit.pl']
TIME_ZONE = 'UTC'

# Application definition

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'login.CustomUser'
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
REGISTRATION_OPEN = getenv('REGISTRATION_OPEN')
REGISTRATION_SALT = getenv('REGISTRATION_SALT')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "ReDesignIT_LOGS.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "HOME": {
            "level": "INFO",
            "handlers": ["file"],
        },
    },
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },

}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'apps.home',
    'apps.projects',
    'apps.about',
    'apps.contact',
    'apps.login',
    'apps.todoapp',
    'apps.shop',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_user_agents',
    'django_recaptcha',
    'django_registration',
    'easy_thumbnails',
    'image_cropping',
]

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
# size is "width x height"
IMAGE_CROPPING_THUMB_SIZE = (500, 500)
IMAGE_CROPPING_SIZE_WARNING = True
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'www_ReDesignIT_pl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'www_ReDesignIT_pl.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DJANGO_DB'),
        'USER': getenv('DJANGO_DB_USER'),
        'PASSWORD': getenv('DJANGO_DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'apps/login/static'),
                    os.path.join(BASE_DIR, 'apps/home/static'),
                    os.path.join(BASE_DIR, 'apps/contact/static'),
                    os.path.join(BASE_DIR, 'apps/about/static'),
                    os.path.join(BASE_DIR, 'apps/projects/static'),
                    os.path.join(BASE_DIR, 'apps/todoapp/static'),
                    os.path.join(BASE_DIR, 'apps/shop/static'),
                    ]
if DEBUG:
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'static'))
    SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
else:
    RECAPTCHA_PUBLIC_KEY = getenv('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = getenv('RECAPTCHA_PRIVATE_KEY')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
