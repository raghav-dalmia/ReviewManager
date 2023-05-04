from userProfile import models as UserModel
from . import models as ReviewModel


def get_review_question(username: str) -> str:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return str(creator.question)


def create_review(username: str, ratings: int, feedback: str, attachments) -> ReviewModel:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    review = ReviewModel.Review.objects.create(creator=creator, ratings=ratings, feedback=feedback)
    for attachment in attachments:
        ReviewModel.ReviewImages.objects.create(review=review, attachments=attachment)
    return review