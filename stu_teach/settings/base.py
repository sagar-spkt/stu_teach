"""
Django settings for stu_teach project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    # 'django.contrib.sites',
    'registration_redux',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'accounts.apps.AccountsConfig',
    'forum.apps.ForumConfig',
    'widget_tweaks',
    'social_django'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

    'stu_teach.middleware.AdminAccessMiddleware',
    'stu_teach.middleware.LoginRequiredMiddleWare',
]

ROOT_URLCONF = 'stu_teach.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <- Here
                'social_django.context_processors.login_redirect', # <- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'stu_teach.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media urls
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'stu_teach/../media')


# INCLUDE_AUTH_URLS = True
# INCLUDE_REGISTER_URL = False

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_FORM = 'registration_redux.forms.CustomRegistrationForm'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


LOGIN_REDIRECT_URL = 'forum:home'
LOGIN_URL = 'auth_login'
LOGOUT_URL = 'auth_logout'

LOGIN_EXEMPT_VIEWS = [
    'landing_page',
    'registration_register',
    'registration_activation_complete',
    'registration_resend_activation',
    'registration_activate',
    'registration_complete',
    'registration_disallowed',
    'auth_password_reset',
    'auth_password_reset_complete',
    'auth_password_reset_done',
    'auth_password_reset_confirm',
    'social:begin',
    'social:complete',
    'social:disconnect',
    'social:disconnect_individual',
]
