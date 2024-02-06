from django.contrib.auth.models import AbstractUser
from django.db import models


class Grouper(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.name)


class Huser(AbstractUser):
    harvardEduIdNumber = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        help_text="HUID",
        verbose_name="harvardEduIdNumber",
    )
    defaultPrincipalId = models.CharField(
        max_length=16,
        help_text="default ID",
        verbose_name="defaultPrincipalId",
        unique=True,
    )
    user = models.CharField(
        max_length=16, help_text="User", verbose_name="user", unique=True, null=True, blank=True, default=None
    )

    netId = models.CharField(
        max_length=16, help_text="netID", verbose_name="netId", unique=True, null=True, blank=True, default=None
    )

    memberOf = models.ManyToManyField(
        Grouper,
        through="MemberOf",
        through_fields=("person", "group"),
    )

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, list(self.memberOf.all()))


class MemberOf(models.Model):
    group = models.ForeignKey(Grouper, on_delete=models.CASCADE)
    person = models.ForeignKey(Huser, on_delete=models.CASCADE)
