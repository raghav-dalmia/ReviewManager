from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True)
    question = models.CharField(max_length=500, null=False, default="Give your feedback.")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

