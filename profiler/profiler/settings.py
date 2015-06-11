"""
Django settings for profiler project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Template Location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "profiler", "templates"),
)

SITE_ID = 1

# Decorator whenever the account is not logged in
LOGIN_URL = '/signin/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ryz-yqwcza745dk_!6uv4@zo3)hpn5&(1@h+(=rabl^!2p_yc'

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
    'accounts',
    # 'django_messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'profiler.urls'

WSGI_APPLICATION = 'profiler.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django_messages.context_processors.inbox',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    )
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE'    : 'mysql.connector.django',
        'NAME'      : 'profiler',
        'USER'      : 'root',
        'PASSWORD'  : '',
        'HOST'      : 'localhost', 
        'PORT'      : '3306',
    },
    # 'students': {
    #     'ENGINE'    : 'django.db.backends.mysql',
    #     'NAME'      : 'elijah_enrollment_system',
    #     'USER'      : 'root',
    #     'PASSWORD'  : 'password',
    #     'HOST'      : 'localhost', 
    #     'PORT'      : '3306',
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "profiler", "static\static")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "profiler", "static\media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "profiler", "static"),
    ) 

# Printing paths for sanity's sake
print ("PROJECT ROOT:", PROJECT_PATH)
print ("TEMPLATES:", TEMPLATE_DIRS)
print ("STATIC:", STATIC_URL)
print ("MEDIA:", MEDIA_URL)