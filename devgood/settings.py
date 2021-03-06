"""
Django settings for devgood project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = BASE_DIR

TEMPLATE_DIRS = (
    PROJECT_PATH,
    PROJECT_PATH + "/layout",
)

##
## EMAIL
##

SERVER_EMAIL = "noreply@devgood.org"
DEFAULT_FROM_EMAIL = "noreply@devgood.org"

# debugging
#EMAIL_HOST = "localhost"
#EMAIL_PORT = 1025

# nixt
#EMAIL_HOST = "nixt.org"
#EMAIL_PORT = 25
#EMAIL_HOST_USER = "devgood%nixt.org"
#EMAIL_HOST_PASSWORD = "Devgood2013"
#EMAIL_USE_TLS = False

# gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "devgood1@gmail.com"
EMAIL_HOST_PASSWORD = "Devgood2013"
EMAIL_USE_TLS = True

########################################


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pylz!4#%1f%ywro)uy*z0e_o$yx&ewl0b^zgl-7@qh$76a&o0l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
    'registration_email.auth.EmailBackend',
)

LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'registration_email',
    'social_auth',
    'messages',
    'devgoodapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'devgood.urls'

WSGI_APPLICATION = 'devgood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
