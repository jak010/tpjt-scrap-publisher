from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class Member(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "member"

    email = models.CharField(
        max_length=36,
        unique=True,
        verbose_name="user_email"
    )

    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    date_of_join = models.DateTimeField(auto_now_add=True, editable=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []
