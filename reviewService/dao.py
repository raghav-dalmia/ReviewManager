from userProfile import models as UserModel
from . import models as ReviewModel


def get_review_question(username: str) -> str:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return str(creator.question)


def create_review(username: str, ratings: int, feedback: str, attachment) -> ReviewModel:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return ReviewModel.Review.objects.create(creator=creator, ratings=ratings, feedback=feedback, attachments=attachment)