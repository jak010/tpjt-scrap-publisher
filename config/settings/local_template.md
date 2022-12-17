# local.py

```text
from .base import *

DEBUG = True

LOCAL_APP = [
    'django_extensions',
    'apps'
]

INSTALLED_APPS += LOCAL_APP

AUTH_USER_MODEL = "apps.Member"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        # 'TEST': { # 테스트를 django test로 할 거면 주석 해제 후 사용
        #     'CHARSET': 'utf8',
        #     'COLLATION': 'utf8_general_ci',
        # }
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'sql': {
            '()': 'django_sqlformatter.SqlFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

```