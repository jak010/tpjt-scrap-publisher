# Toy Project

## Description

- 구독한 블로그를 그룹끼리 공유하자

# Functional

- 사용자 등록
- 사용자 삭제
- 사용자 그룹 등록
- 사용자 그룹 멤버 등록
- RSS 수집

# Setup

## AbstractBaseUser Model

```text
AUTH_USER_MODEL = "apps.Member"
```

## Django Email Setup

```text
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

## SQL Logging

```text
# SQL LOGGING
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