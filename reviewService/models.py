import os
import time
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils import timezone
from userProfile.models import Creator
from django.core.exceptions import ValidationError


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (int(time.time()), ext)
    return os.path.join('reviews', filename)


def resize_image(image):
    # Open the image using Pillow
    img = Image.open(image)

    # Set the maximum width and height for the resized image
    max_size = (800, 800)

    # Resize the image while maintaining the aspect ratio
    img.thumbnail(max_size)

    # Create a BytesIO object to temporarily hold the resized image
    output = BytesIO()

    # Convert RGBA image to RGB mode if necessary
    if img.mode == 'RGB':
        img.save(output, format='JPEG', quality=70)
        resized_image = InMemoryUploadedFile(
            output,
            'ImageField',
            f"{image.name.split('.')[0]}.jpg",
            'image/jpeg',
            output.tell(),
            None
        )
    elif img.mode == 'RGBA':
        img.save(output, format='PNG', quality=70)
        resized_image = InMemoryUploadedFile(
            output,
            'ImageField',
            f"{image.name.split('.')[0]}.png",
            'image/jpeg',
            output.tell(),
            None
        )

    return resized_image


class Review(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    reviewee = models.CharField(max_length=200, blank=True, default="Anonymous")
    ratings = models.PositiveSmallIntegerField(null=False)
    packaging = models.TextField(max_length=1500, null=True, blank=True)
    feedback = models.CharField(max_length=1500, default="How's the packaging experience?", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.pk) + " - " + str(self.creator.user.username)

    def clean(self):
        if self.ratings < 1 or self.ratings > 5:
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
        if not self.pk:
            self.created_on = timezone.now()
        return super().save(*args, **kwargs)


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    attachment = models.ImageField(upload_to=get_file_path, max_length=50, null=True)

    class Meta:
        ordering = ["-pk"]

    def save(self, *args, **kwargs):
        # if self.attachment:
        #     self.attachment = resize_image(self.attachment)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.review.pk) + " - " + str(self.pk)
