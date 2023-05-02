import os
import time
from django.db import models
from userProfile.models import Creator


def get_file_path(instance, filename):
    print(filename)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (int(time.time()), ext)
    return os.path.join('reviews', filename)


class Review(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    reviewee = models.CharField(max_length=200, null=True)
    # ratings = models.PositiveSmallIntegerField(null=False)
    packaging = models.TextField(max_length=1500, null=True)
    feedback = models.CharField(max_length=1500, null=True)
    attachments = models.FileField(upload_to=get_file_path, max_length=300, null=True)
