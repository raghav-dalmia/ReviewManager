import os
import time
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from . import utils
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def get_file_path(instance, filename):
    name, ext = filename.split('.')
    filename = filename if name == "default" else "%s_%s.%s" % (str(instance.user.id), name, ext)
    return os.path.join('profile', filename)


class ORDERING_TYPE(models.IntegerChoices):
    BEST = 1, '-ratings'
    LATEST = 2, '-created_on'
    OLDEST = 3, 'created_on'


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


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=get_file_path, max_length=50, default='default.png')
    description = models.CharField(max_length=255, default="", blank=True)
    question = models.CharField(max_length=500, null=True, blank=True)
    resultsToDisplay = models.PositiveIntegerField(default=5, null=False, blank=False)
    orderBy = models.IntegerField(default=ORDERING_TYPE.BEST, choices=ORDERING_TYPE.choices, null=False, blank=False)
    instagram_url = models.URLField(max_length=300, blank=True)
    youtube_url = models.URLField(max_length=300, blank=True)
    linkedin_url = models.URLField(max_length=300, blank=True)
    facebook_url = models.URLField(max_length=300, blank=True)
    website_url = models.URLField(max_length=300, blank=True)
    twitter_url = models.URLField(max_length=300, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def clean(self):
        # if not utils.validPhoneNumber(self.phone_number):
        #     raise ValidationError({'phonenumber': 'Oops, you entered invalid phone number :('})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.pk:
            self.last_updated = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_orderby_clause(self) -> str:
        return ORDERING_TYPE(self.orderBy).label
