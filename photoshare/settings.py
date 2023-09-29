"""
Django settings for photoshare project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

RUN_SERVER_PORT = 8000

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ \
    else 'django-insecure-#8j@swzfo((go@@)31+cr^z97ljrvyplx2(7b2oe-u#=6&cc_$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG'] == "True" if "DEBUG" in os.environ else True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'picnet.me',
    'photo-share-app.net',
    'photoshare-dev.us-west-2.elasticbeanstalk.com',
    '.vercel.app'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'django.contrib.postgres',
    'ebhealthcheck.apps.EBHealthCheckConfig',
    'algoliasearch_django',
    'strawberry.django',
    "strawberry_django",
    "debug_toolbar",
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'strawberry_django.middlewares.debug_toolbar.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'photoshare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'photoshare.wsgi.app'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
elif 'POSTGRES_HOST' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRES_DATABASE'],
            'USER': os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST': os.environ['POSTGRES_HOST'],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "photoshare",
            'USER': 'postgres',
            'PASSWORD': 'example',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = "static/"

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage' if DEBUG \
    else 'storages.backends.s3boto3.S3StaticStorage'

STATICFILES_DIRS = [
    "frontend/dist",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = "media/"

MEDIA_ROOT = "media/"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage' if DEBUG \
    else 'storages.backends.s3boto3.S3Boto3Storage'

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

AWS_ACCESS_KEY_ID = os.environ['AWS_PHOTO_SHARE_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_PHOTO_SHARE_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = "photo-share-app-storage"

AWS_S3_CUSTOM_DOMAIN = 'd1mwzc9v8ocr0h.cloudfront.net'

AWS_S3_REGION_NAME = 'us-west-2'

AWS_LOCATION = 'static/'

AWS_S3_FILE_OVERWRITE = False

ALGOLIA = {
    'APPLICATION_ID': os.environ["ALGOLIA_APPLICATION_ID"],
    'API_KEY': os.environ["ALGOLIA_API_KEY"],
    'INDEX_PREFIX': "photo_share",
    'INDEX_SUFFIX': "dev" if DEBUG else "prod"
}

INTERNAL_IPS = [
    "127.0.0.1",
]

STRAWBERRY_DJANGO = {
    "MAP_AUTO_ID_AS_GLOBAL_ID": True,
}
