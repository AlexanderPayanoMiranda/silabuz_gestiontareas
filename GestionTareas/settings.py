"""
Django settings for GestionTareas project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# DO NOT PUSH TO REPOSITORY
SECRET_KEY = 'django-insecure-se2l&hr!f%+z^xkhf$)m=x)zpd+qpe2a3m69=1xr+4o_dl5c5y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DO NOT PUSH TO REPOSITORY
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'vitrina.apps.VitrinaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GestionTareas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'GestionTareas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # DO NOT PUSH TO REPOSITORY
        'NAME': 'gestion_tareas',
        # DO NOT PUSH TO REPOSITORY
        'USER': 'root',
        # DO NOT PUSH TO REPOSITORY
        'PASSWORD': 'jV#%rh5ujnX3kSnBg#xYEP7L',
        # DO NOT PUSH TO REPOSITORY
        'HOST': 'localhost',
        # DO NOT PUSH TO REPOSITORY
        'PORT': '3306'
    }
}


# Email Settings
# Modify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD to your own email to send emails
# Using Outlook SMTP server instead of Gmail
# The SMTP server  of Gmail not working properly
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# DO NOT PUSH TO REPOSITORY
EMAIL_HOST_USER = 'randommail'
# DO NOT PUSH TO REPOSITORY
EMAIL_HOST_PASSWORD = 'randompassword'


# Celery settings
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cache Sessions Engine
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# PYMEMCACHE CACHE
# To be able to use memcache, you need to install memcached on your platform
# Releases for Windows can be found on https://github.com/jefyt/memcached-windows/releases/tag/1.6.8_mingw
# The following command are used when using Memcached
# path_to_memcached\memcached.exe -d install
# path_to_memcached\memcached.exe -d start
# path_to_memcached\memcached.exe -d stop
CACHES = {
    'default': {
        # Following documentation update, using pip install pymemcache
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        # DO NOT PUSH TO REPOSITORY
        'LOCATION': ['127.0.0.1:11211', '127.0.0.2:11211', '127.0.0.3:11211'],
    }
}


# DB CACHE
# Before using, you need to create the cache table with:
# python manage.py createcachetable
# The name of the table is taken from the LOCATION variable below.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # DO NOT PUSH TO REPOSITORY
#         'LOCATION': 'my_cache_table',
#     }
# }


# FILESYSTEM CACHE
# The configuration below will save the cache to the path shown below.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # DO NOT PUSH TO REPOSITORY
#         'LOCATION': 'D:/django_cache',
#     }
# }
