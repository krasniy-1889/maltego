import os
from pathlib import Path
from dotenv import load_dotenv

# load .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c@+o-xa!ts#)8hv2l&-=ep3@hxq2ie8w8k258h1+xvaochl=@("


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ! Debug
    "django_browser_reload",
    "debug_toolbar",
    # * Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    # * Application
    # "taggit",
    "django_filters",
    "django_extensions",
    "storages",
    "apps.core",
    "apps.user",
    "apps.post",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    # ! Debug
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "maltego.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # * Custom
                "apps.core.context_processors.url_name",
            ],
        },
    },
]

WSGI_APPLICATION = "maltego.wsgi.application"


# Allauth providers settings
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "APP": {
            "client_id": os.environ.get("GITHUB_CLIENT_ID"),
            "secret": os.environ.get("GITHUB_CLIENT_SECRET"),
            "key": "",
        },
    }
}

# Authentication
AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

# REST Framework
# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
#     ],
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]


AUTH_USER_MODEL = "user.CustomUser"

# Sessions
SESSION_ENGINE = "redis_sessions.session"
SESSION_REDIS = {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "password": "",
    "prefix": "session",
    "socket_timeout": 1,
    "retry_on_timeout": False,
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "logstash": {
            "level": "DEBUG",
            "class": "logstash.TCPLogstashHandler",
            "host": "logstash",
            "port": 6000,
            "version": 1,
            "message_type": "django",
            "fqdn": False,
            "tags": ["django.request"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["logstash"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
# STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "media/"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
