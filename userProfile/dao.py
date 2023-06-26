from . import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def create_creator(username: str, password: str) -> models.Creator:
    user = User.objects.create_user(username=username, password=password)
    return models.Creator.objects.create(user=user)


def get_creator(user: User) -> models.Creator:
    try:
        return models.Creator.objects.get(user__username__exact=user.username)
    except ObjectDoesNotExist:
        return models.Creator.objects.create(user=user)


def get_creator_from_username(username: str) -> models.Creator:
    user = User.objects.get(username=username)
    return models.Creator.objects.get(user=user)


def update_creator(user: User, description: str, instagram: str, linkedin: str, email: str,
                   firstname: str, lastname: str, question: str, numberOfResults: int, orderBy: int, facebook: str,
                   profile_picture, website: str, youtube: str, twitter: str) -> models.Creator:
    creator = get_creator_from_username(user)
    creator.description = description
    creator.instagram_url = instagram
    creator.linkedin_url = linkedin
    creator.facebook_url = facebook
    creator.youtube_url = youtube
    creator.website_url = website
    creator.twitter_url = twitter
    creator.user.email = email
    creator.user.first_name = firstname
    creator.user.last_name = lastname
    creator.question = question
    creator.resultsToDisplay = numberOfResults
    creator.orderBy = orderBy
    if profile_picture:
        creator.profile_picture = profile_picture
    creator.user.save()
    creator.save()
    creator.user.save()
    return creator
