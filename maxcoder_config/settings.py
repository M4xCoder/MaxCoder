"""
Using Django 2.2.6.
Using Python 3.7.4

"""
try:
    from .dev_settings import *
except ImportError:
    from .prod_settings import *

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.accounts',  # My application. Is put ahead allauth, to replace patterns.
    # Download application.
    'analytical',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    # My application.
    'apps.home_page',
    'apps.blog',
    'apps.shop',
]

# Allauth settings

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 60

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'maxcoder_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'maxcoder_config/templates')],
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

WSGI_APPLICATION = 'maxcoder_config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#################################################3
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'src/static/')  # Путь для сбора всех статических файлов

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'src/media/')  # Путь для хранения загружаемых данных проекта

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'maxcoder_config/static/')]

#LOGIN_URL = "/auth/login/"  #прямая ссылка на страницу входа
#LOGIN_URL = "authapp:login"  #ссылка на страницу входа через имя указанное в привязке url
#LOGOUT_URL = "authapp:logout"  #ссылка на страницу выхода через имя указанное в привязке url
#LOGIN_REDIRECT_URL = "/certificates/" #прямая ссылка на страницу перенаправления после успешного входа


YANDEX_METRICA_COUNTER_ID = '00000000'

