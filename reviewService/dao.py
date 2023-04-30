from userProfile import models as UserModel
from . import models as ReviewModel


def get_review_question(username: str) -> str:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return str(creator.question)


def create_review(username: str, feedback: str, reviewee: str, packaging: str, attachment) -> ReviewModel:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return ReviewModel.Review.objects.create(creator=creator, feedback=feedback, reviewee=reviewee, packaging=packaging, attachments=attachment)