from userProfile import models as UserModel
from . import models as ReviewModel


def get_review_question(username: str) -> str:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    return str(creator.question)


def create_review(username: str, feedback: str, reviewee: str, packaging: str, ratings: int, attachments) -> ReviewModel:
    creator = UserModel.Creator.objects.get(user__username__exact=username)
    review = ReviewModel.Review.objects.create(creator=creator, feedback=feedback, reviewee=reviewee, packaging=packaging, ratings=ratings)
    for attachment in attachments:
        ReviewModel.ReviewImage.objects.create(review=review, attachment=attachment)
    return review
