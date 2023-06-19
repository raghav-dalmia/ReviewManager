import os
import time
from . import utils
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (int(time.time()), ext)
    return os.path.join('profile', filename)


class ORDERING_TYPE(models.IntegerChoices):
    BEST = 1, '-ratings'
    LATEST = 2, '-created_on'
    OLDEST = 3, 'created_on'


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="", blank=True)
    question = models.CharField(max_length=500, default="We want to hear more", null=False, blank=False)
    resultsToDisplay = models.PositiveIntegerField(default=5, null=False, blank=False)
    orderBy = models.IntegerField(default=ORDERING_TYPE.BEST, choices=ORDERING_TYPE.choices, null=False, blank=False)
    instagram_url = models.URLField(max_length=300, blank=True)
    linkedin_url = models.URLField(max_length=300, blank=True)
    facebook_url = models.URLField(max_length=300, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def clean(self):
        # if not utils.validPhoneNumber(self.phone_number):
        #     raise ValidationError({'phonenumber': 'Oops, you entered invalid phone number :('})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_orderby_clause(self) -> str:
        return ORDERING_TYPE(self.orderBy).label
