from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'np9&!lf+*ezh6)z@m6iw_^g0lr4g%g08oc6m5^n#4t9a4z(-%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['covid.put.poznan.pl']

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_modal_forms',
    'compressor',
    'front',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'csp.middleware.CSPMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'forms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'forms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covid_forms',
        'USER': 'covid_forms',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "unix:/var/sockets/redis.sock",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "covidcache"
    }
}

CELERY_BROKER_URL = 'redis+socket:///var/sockets/redis.sock'
CELERY_TIMEZONE = "Europe/Warsaw"
# CELERY_BEAT_SCHEDULE = {
#     'mailing': {
#         'task': 'mailing',
#         'schedule': 10.0,
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pl-pl'
LANGUAGES = (  # supported languages
    ('en', 'English'),
    ('pl', 'Polish'),
)

LOCALE_PATHS = [
    BASE_DIR / "front/locale",
    BASE_DIR / "locale",
]

FORMAT_MODULE_PATH = [
    'forms.formats',
]

TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = 'static_root'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'DENY'

EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "Biuro ds. COVID-19 <biurocovid@put.poznan.pl>"
SERVER_EMAIL = "COVID Forms App <biurocovid@put.poznan.pl>"

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000 # TODO: enable once tested
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

COMPRESS_ENABLED = True
COMPRESS_URL = "/static/"
COMPRESS_OUTPUT_DIR = "compressed"
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'strict-dynamic'"]
CSP_STYLE_SRC = ["'self'"]
CSP_IMG_SRC = ["'self'"]
CSP_CONNECT_SRC = ["'self'"]
CSP_FRAME_SRC = ["'self'"]
CSP_INCLUDE_NONCE_IN = [
    "default-src",
    "script-src",
    "style-src",
]

COMPRESS_CSP_NONCE = True

from .secrets import *
