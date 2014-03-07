"""
Django settings for spreadsheet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, '..')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&iq6tme*pcj+3s3^b0deb@q*#e8k3@&x3cmw5qw%)21m=^ao4m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sheets',
    'south',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'spreadsheet.urls'

WSGI_APPLICATION = 'spreadsheet.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'spreadsheet', 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'spreadsheet', 'static')
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'spreadsheet', 'static'),)

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
)
#login
LOGIN_REDIRECT_URL = '/sheets/'

#email
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

#3rd party
ACCOUNT_ACTIVATION_DAYS = 7


#Heroku stuff might need to edit above stuff

# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
# 
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# 
# # Allow all host headers
# ALLOWED_HOSTS = ['*']
# 
# # Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
# 
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
