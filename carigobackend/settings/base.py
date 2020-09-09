from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
PROJECT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
sys.path.insert(0, os.path.join(PROJECT_DIR, "apps"))

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party apps
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount'
]

CARGO_APPS = ["main", "accounts"]

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = list(set(DJANGO_APPS + CARGO_APPS))

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carigobackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'carigobackend.wsgi.application'

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


# custom user settings
AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# rest_framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # all views are write protected unless otherwise stated
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':
    [  # 'rest_framework.authentication.SessionAuthentication',   # allow for authentication within rest framework GUI
        'rest_framework.authentication.BasicAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'carigoauthkey'
SITE_ID = 1
REST_AUTH_REGISTER_SERIALIZERS = {
    # custom registration serializers to include custom user fields
    'REGISTER_SERIALIZER': 'accounts.serializers.RegistrationSerializer'}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

LOGIN_REDIRECT_URL = "/dashboard/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
