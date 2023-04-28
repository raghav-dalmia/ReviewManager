from . import models
from django.contrib.auth.models import User


def create_creator(username: str, password: str) -> models.Creator:
    user = User.objects.create_user(username=username, password=password)
    return models.Creator.objects.create(user=user)


def get_creator(user: User) -> models.Creator:
    return models.Creator.objects.get(user__username__exact=user.username)
