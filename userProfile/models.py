from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):

    class ORDERING_TYPE(models.IntegerChoices):
        BEST = 1
        LATEST = 2
        OLDEST = 3

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="")
    question = models.CharField(max_length=500, default="")
    resultsToDisplay = models.IntegerField(default=1)
    orderBy = models.IntegerField(default=ORDERING_TYPE.BEST)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

