"""
Django settings for production_simulator project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import psycopg2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '14z7s_bd1h&-_6hsb6u(ptc9u3*vzs+(84^19j4!sxz&&7^nxg'

# SECURITY WARNING: don't run with debug turned on in production!
# !!! PRODUCTION
DEBUG = False
# !!! ALLOW hosts
ALLOWED_HOSTS = ['***']

# Application definition

INSTALLED_APPS = [
    'informations',
    'erp',
    'users.apps.UsersConfig',   # otherwise signals wont work
    'crispy_forms',
    'django_filters',
    'bootstrapform',
    'phonenumber_field',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # !!! connect S3
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # !!! for creating staticfiles thru whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'production_simulator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'production_simulator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# !!! connect to AWS DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '***',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # updates Bootstrap for crispy

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

LOGIN_REDIRECT_URL = 'informations-home'  # redirect after login needs to be specific

LOGOUT_REDIRECT_URL = "informations-home"

LOGIN_URL = 'login'  # if user is not login there he wil be sent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# email informations @-less security
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
EMAIL_PORT = 587

PHONENUMBER_DB_FORMAT = 'E164'

# you can do this by environment variable
# !!! connect to S3 bucket
AWS_ACCESS_KEY_ID = Access = '***'
AWS_SECRET_ACCESS_KEY = Secret = '***'
AWS_STORAGE_BUCKET_NAME = '***'

# !!! connect S3 settings
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_FILE_OVERWRITE = False # True-overwrites exisiting files
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # connect for boto3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # django prioritize files from S3
