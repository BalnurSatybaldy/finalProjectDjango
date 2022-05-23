"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_qu37sseycb7+q3uu32-pfbo-!3$2(1e9go#azl5ua6-a)n!oz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'charity',
    'trustfund',
    'volunteer',
    'chat'
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/profile/'

IOKA_CREATE_ORDER_URL = "https://stage-api.ioka.kz/v2/orders"
IOKA_REQUEST_HEADER = {"API-KEY": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE3NjQxNDk2MDcsImlhdCI6MTY0MzM0OTg0OSwiYXpwIjoiZGFzaGJvYXJkIiwiaXNzIjoiZ2FybWl1cyIsInN1YiI6InVzcl9hNDNhMmU3NC0zYWUzLTRmOGMtYTk2Ni03NjA2NTNkOGFjODQiLCJhdWQiOlsidG9rZW5pemVyIiwiY29yZSIsInNwbGl0IiwiY3VzdG9tZXIiLCJpZGVudGl0eSIsIndhbGxldCJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsidG9rZW5pemVyIjp7InJvbGVzIjpbInBheW1lbnQtbWV0aG9kczp3cml0ZSJdfSwiY29yZSI6eyJyb2xlcyI6WyJvcmRlcnM6d3JpdGUiLCJvcmRlcnM6cmVhZCIsIm9yZGVycy4qLnBheW1lbnRzOndyaXRlIiwib3JkZXJzLioucGF5bWVudHM6cmVhZCIsIm9yZGVycy4qLnBheW1lbnRzLioucmVmdW5kczp3cml0ZSIsIm9yZGVycy4qLnBheW1lbnRzLioucmVmdW5kczpyZWFkIiwid2ViaG9va3M6d3JpdGUiLCJ3ZWJob29rczpyZWFkIiwic3Vic2NyaXB0aW9uczp3cml0ZSIsInN1YnNjcmlwdGlvbnM6cmVhZCIsInN1YnNjcmlwdGlvbnMuKi5vcmRlcnMuKi5wYXltZW50czp3cml0ZSIsInN1YnNjcmlwdGlvbnMuKi5vcmRlcnMuKi5wYXltZW50czpyZWFkIl19LCJzcGxpdCI6eyJyb2xlcyI6WyJzcGxpdHM6cmVhZCIsInNwbGl0czp3cml0ZSIsInNwbGl0czpyZW1vdmUiLCJzcGxpdHMuZXZlbnRzOnJlYWQiLCJzcGxpdHMud2ViaG9va3M6d3JpdGUiLCJzcGxpdHMud2ViaG9va3M6cmVhZCIsInNwbGl0cy53ZWJob29rczpyZW1vdmUiXX0sImN1c3RvbWVyIjp7InJvbGVzIjpbImN1c3RvbWVyczp3cml0ZSIsImN1c3RvbWVyczpyZWFkIiwiY3VzdG9tZXJzLiouY2FyZHM6d3JpdGUiLCJjdXN0b21lcnMuKi5jYXJkczpyZWFkIl19LCJpZGVudGl0eSI6eyJyb2xlcyI6WyJpZGVudGl0aWVzLmNsYXNzZXM6cmVhZCIsImlkZW50aXRpZXMuY2xhc3Nlczp3cml0ZSIsImlkZW50aXRpZXMuY2xhc3NlczpyZW1vdmUiLCJpZGVudGl0aWVzOnJlYWQiLCJpZGVudGl0aWVzOndyaXRlIiwiaWRlbnRpdGllczpyZW1vdmUiXX0sIndhbGxldCI6eyJyb2xlcyI6WyJ3YWxsZXRzOnJlYWQiLCJ3YWxsZXRzOndyaXRlIiwid2FsbGV0czpyZW1vdmUiLCJ3YWxsZXRzLmFjY291bnQ6cmVhZCIsIndhbGxldHMuZXZlbnRzOnJlYWQiLCJ3YWxsZXRzLnRyYW5zYWN0aW9uczpyZWFkIiwid2FsbGV0cy50cmFuc2FjdGlvbnM6d3JpdGUiLCJ3YWxsZXRzLnRyYW5zYWN0aW9uczpyZW1vdmUiLCJ3YWxsZXRzLncydzp3cml0ZSIsIndhbGxldHMudzJ3OnJlYWQiLCJ3YWxsZXRzLndlYmhvb2tzOndyaXRlIiwid2FsbGV0cy53ZWJob29rczpyZWFkIiwid2FsbGV0cy53ZWJob29rczpyZW1vdmUiLCJ3aXRoZHJhd2FsczpyZWFkIiwid2l0aGRyYXdhbHM6d3JpdGUiLCJ3aXRoZHJhd2FsczpyZW1vdmUiXX19LCJ1c2VyIjp7ImlkIjoidXNyX2E0M2EyZTc0LTNhZTMtNGY4Yy1hOTY2LTc2MDY1M2Q4YWM4NCIsImRpc3BsYXlfbmFtZSI6IkFpa3VtaXMgS2FsaSIsInVzZXJuYW1lIjoiYS5rYWxpQGlva2Eua3oiLCJmaXJzdF9uYW1lIjoiQWlrdW1pcyIsImxhc3RfbmFtZSI6IkthbGkiLCJlbWFpbCI6ImEua2FsaUBpb2thLmt6Iiwic3RhdHVzIjoiQUNUSVZFIn0sInNob3AiOnsiaWQiOiJzaHBfWk5DUlI3UEMyRyIsIm93bmVyX2lkIjoidXNyX2E0M2EyZTc0LTNhZTMtNGY4Yy1hOTY2LTc2MDY1M2Q4YWM4NCIsImJpbiI6IjMxMzEzMiIsImRpc3BsYXlfbmFtZSI6InRlc3QiLCJzdGF0dXMiOiJBQ0NFUFRFRCJ9LCJsb2NhbGUiOiJydSJ9.XUCaRZbWQ2cNs2tb-JiN8ghcStnXW6dgwzn8-LkhDciTXGHL3LHVXc2ZWdxsWXBild5EM85tlBC3RawJzpvMMpBaZOTxF-fdAsmwOMYGHpNv7nmuC8Ne2LRia1Rn92SydPQumPxLueIoN5pNHCMBEl6SxE4lxRXv-BPtG3Tu-Wlx98-Veta2eT04V6-jpKQGNpUNNQVn8dvzzY7Viw49jbOb_YaJfdaz6jygIiAU08vqIyRL-t6JjfD1Xr67BM1pxK-rfq6Z0rHRvEFC5kHnYO3CKGj8zP03xs3tdz995AWpj_rscSQweJ4qstJsSKfwABQZpoc3ktz17BGgRdY1gg"}
