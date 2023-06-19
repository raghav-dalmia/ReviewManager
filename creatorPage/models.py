from django.db import models
from userProfile.models import Creator


class PageView(models.Model):
    creator = models.ForeignKey(Creator, editable=False, on_delete=models.CASCADE)
    date = models.DateField(editable=False)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.creator.user.username + " " + str(self.date)
