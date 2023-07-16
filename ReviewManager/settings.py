"""
Django settings for ReviewManager project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from aws_config.creds import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rtgh-2iy90^qeproj&^unla9dlm9a)bs2tpus-8x*-6$wx*1)g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PROD_SERVER
LOCAL_ENV = PROD_SERVER

if LOCAL_ENV:
    ALLOWED_HOSTS = ['127.0.0.1']
else:
    ALLOWED_HOSTS = [DOMAIN_NAME, PUBLIC_IP, 'www.'+DOMAIN_NAME, SUBDOMAIN_NAME+'.'+DOMAIN_NAME]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # all auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',

    # my custom apps
    'appAuth',
    'userProfile',
    'reviewService',
    'creatorPage',
]

LOGIN_REDIRECT_URL = 'creatorAnalytics'
# ACCOUNT_LOGOUT_ON_GET = True
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_LOGIN_ON_GET = True


# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         "SCOPE": [
#             "profile",
#             "email",
#         ]
#     }
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.RequestUpdater.RequestUpdater',
    # 'middleware.logExceptionMiddleware.LogRequestExceptionMiddleware',
]

ROOT_URLCONF = 'ReviewManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'context_processors.context_processors.global_constants',
            ],
        },
    },
]

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

WSGI_APPLICATION = 'ReviewManager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if LOCAL_ENV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': DATABASE_ENGINE,
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'ReviewManager'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

if LOCAL_ENV:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    AWS_ACCESS_KEY_ID = ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME = STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = DEFAULT_ACL
    AWS_S3_SIGNATURE_NAME = S3_SIGNATURE_NAME
    AWS_S3_REGION_NAME = S3_REGION_NAME
    AWS_S3_CUSTOM_DOMAIN = S3_CUSTOM_DOMAIN
    AWS_S3_OBJECT_PARAMETERS = S3_OBJECT_PARAMETERS
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = MEDIA_LOCATION
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'aws_config.storage_backends.PublicMediaStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `account`
    'django.contrib.auth.backends.ModelBackend',

    # `account` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# LOGGING = {
#     "version": 1,
#     'disable_existing_loggers': False,
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": "error.log",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "ERROR",
#             "propagate": True,
#         },
#     },
# }