from . import models
from django.contrib.auth.models import User


def create_creator(username: str, password: str) -> models.Creator:
    user = User.objects.create_user(username=username, password=password)
    return models.Creator.objects.create(user=user)


def get_creator(user: User) -> models.Creator:
    try:
        return models.Creator.objects.get(user__username__exact=user.username)
    except:
        return models.Creator.objects.create(user=user)


def update_creator(user: User, description: str, phonenumber: int, instagram: str, linkedin: str, email: str,
                   firstname: str, lastname: str, question: str, numberOfResults: int, orderBy: int) -> models.Creator:
    creator = get_creator(user)
    creator.description = description
    creator.phone_number = phonenumber
    creator.instagram_id = instagram
    creator.linkedin_id = linkedin
    creator.user.email = email
    creator.user.first_name = firstname
    creator.user.last_name = lastname
    creator.question = question
    creator.resultsToDisplay = numberOfResults
    creator.orderBy = orderBy
    creator.user.save()
    creator.save()
    creator.user.save()
    return creator
