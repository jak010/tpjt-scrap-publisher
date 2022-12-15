# Toy Project

## Description

- 기사 하나를 스크랩하여 특정 사용자의 이메일로 전송해주자.

# Functional

- 사용자 등록
- 사용자 삭제
- 이메일 그룹 등록
- 이메일 그룹 삭제
- 이메일 그룹 멤버 등록
- 이메일 그룹 멤버 삭제

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