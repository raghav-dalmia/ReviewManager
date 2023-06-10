from django.db import models
from django.contrib.auth.models import User

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
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_orderby_clause(self) -> str:
        return ORDERING_TYPE(self.orderBy).label


