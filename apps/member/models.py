from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.utils.translation import gettext_lazy as _


class Member(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "member"
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    email = models.CharField(
        max_length=36,
        unique=True,
        verbose_name="email"
    )

    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    date_of_join = models.DateTimeField(auto_now_add=True, editable=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []


class MemberInvitation:
    class Meta:
        db_table = "member_invitation"
        verbose_name = '사용자 초대 링크'

    email = models.CharField(
        max_length=36,
        unique=True,
        verbose_name="email"
    )
    invitation_code = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="email_verify_code",
        null=False
    )

    exp_time = models.DateTimeField(
        verbose_name="iat_time",
        blank=False,
        null=False
    )

    send_time = models.DateTimeField(
        verbose_name="iat_time",
        blank=False,
        null=False
    )
