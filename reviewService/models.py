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
    ratings = models.PositiveSmallIntegerField(null=False)
    feedback = models.CharField(max_length=1500, null=True)

    def __str__(self) -> str:
        return str(self.pk) + ": " + self.feedback


class ReviewImages(models.Model):
    attachments = models.ImageField(upload_to=get_file_path, max_length=300, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.review.pk) + ": " + self.review.feedback
