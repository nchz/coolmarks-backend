import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
DEBUG = True
SECRET_KEY = "($39x(vd=1$1uc%nzq7!xrd*$uz0+0v*qsy2+3&oc&9#8q@^k3"
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "chrome-extension://akmmjffnhjjcmaljijffnllflkbpofle",
]


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "collectstatic"
STATICFILES_DIRS = [BASE_DIR / "static"]

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/api/links/"
LOGOUT_REDIRECT_URL = "/"

# Used by allauth.
SITE_ID = 1
ACCOUNT_LOGOUT_ON_GET = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# TODO Check if actually needed.
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Dependencies.
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.google",
    # Project apps.
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "coolmarks.urls"
WSGI_APPLICATION = "coolmarks.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data" / "db.sqlite3",
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
_VALIDATORS_PREFIX = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{_VALIDATORS_PREFIX}.UserAttributeSimilarityValidator"},
    # {"NAME": f"{_VALIDATORS_PREFIX}.MinimumLengthValidator"},
    # {"NAME": f"{_VALIDATORS_PREFIX}.CommonPasswordValidator"},
    {"NAME": f"{_VALIDATORS_PREFIX}.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Extension specific.

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": None,
    "DEFAULT_RENDERER_CLASSES": [
        # "rest_framework.renderers.TemplateHTMLRenderer",
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}


# Production settings.

if os.getenv("ENV") == "prod":
    DEBUG = False
    ALLOWED_HOSTS = ["coolmarks.duckdns.org"]
