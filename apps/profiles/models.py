from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampModel, UUIDModel


class UserProfile(UUIDModel, TimeStampModel):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    GENDER_CHOICES = [(MALE, _(MALE)), (FEMALE, _(FEMALE)), (OTHER, _(OTHER))]

    user = models.OneToOneField(
        AUTH_USER_MODEL, related_name="userprofile", on_delete=models.CASCADE
    )
    first_name = models.CharField(_("First Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True)
    gender = models.CharField(
        _("Gender"), choices=GENDER_CHOICES, max_length=20, default=OTHER
    )

    class Meta:
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return f"{self.user.username}'s profile"

    @property
    def get_username(self):
        return self.user.username
