from django.utils.translation import gettext_lazy as _
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-uis!_s6dy=(if+04qko-syq($%s&d%1lu7xp2u-09j7e9+kpvn'


DEBUG = False






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'modeltranslation',    #переводчик model   pip install django-modeltranslation
    'hands.apps.HandsConfig', #приложение
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  #перевод
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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

LANGUAGES = [
    ('uk', _('Українська')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'uk'

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

USE_I18N = True
USE_L10N = True
USE_TZ = True
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'  # Основной язык для modeltranslation
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uk', 'en')


# LANGUAGE_CODE = 'uk'  
# TIME_ZONE = 'Europe/Kiev'  
# USE_I18N = True
# USE_TZ = True



STATIC_URL = 'static/'

CSRF_TRUSTED_ORIGINS = ['https://handsmercy.pythonanywhere.com']

ALLOWED_HOSTS = ['Handsmercy.pythonanywhere.com','localhost', '127.0.0.1']
# ALLOWED_HOSTS = ['*']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
