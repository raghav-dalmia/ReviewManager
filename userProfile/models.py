from . import utils
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Creator(models.Model):
    user = models.OneToOneField(User, editable=False, blank=False, on_delete=models.CASCADE)
    instagram_id = models.CharField(max_length=200, blank=True)
    linkedin_id = models.CharField(max_length=200, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, default="")
    question = models.CharField(max_length=1500, null=False, blank=False, default="Give your feedback.")
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=False)

    def clean(self):
        if not utils.validPhoneNumber(self.phone_number):
            raise ValidationError({'phonenumber': 'Oops, you entered invalid phone number :('})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
