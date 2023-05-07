import os
import time
from django.db import models
from userProfile.models import Creator
from django.core.exceptions import ValidationError



def get_file_path(instance, filename):
    print(filename)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (int(time.time()), ext)
    return os.path.join('reviews', filename)


class Review(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    reviewee = models.CharField(max_length=200, blank=True, default="Anonymous")
    ratings = models.PositiveSmallIntegerField(null=False)
    packaging = models.TextField(max_length=1500, null=True, blank=True)
    feedback = models.CharField(max_length=1500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.pk) + " - " + str(self.creator.user.username)

    def clean(self):
        if self.ratings<1 or self.ratings>5:
            raise ValidationError({'ratings': 'ratings rages: 0 to 5.'})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.reviewee is None:
            self.reviewee = "Anonymous"
        else:
            self.reviewee = self.reviewee.strip()
            if len(self.reviewee) == 0:
                self.reviewee = "Anonymous"
        return super().save(*args, **kwargs)


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=get_file_path, max_length=300, null=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return str(self.review.pk) + " - " + str(self.pk)

