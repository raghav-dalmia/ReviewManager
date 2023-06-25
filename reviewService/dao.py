from datetime import date, timedelta
from django.db.models import Avg
from userProfile import dao as UserDao
from . import models as ReviewModel


def get_review_question(username: str) -> str:
    creator = UserDao.get_creator_from_username(username=username)
    return str(creator.question)


def create_review(username: str, feedback: str, reviewee: str, packaging: str, ratings: int,
                  attachments) -> ReviewModel:
    creator = UserDao.get_creator_from_username(username=username)
    review = ReviewModel.Review.objects.create(creator=creator, feedback=feedback, reviewee=reviewee,
                                               packaging=packaging, ratings=ratings)
    for attachment in attachments:
        ReviewModel.ReviewImage.objects.create(review=review, attachment=attachment)
    return review


def get_review_context(username: str) -> dict:
    creator = UserDao.get_creator_from_username(username=username)
    reviews = ReviewModel.Review.objects.order_by(creator.get_orderby_clause())[:creator.resultsToDisplay]
    return {
        "creatorDetail": creator,
        "reviews": reviews
    }


def get_review_form_view_context(username: str, num_days: int) -> dict:
    start_date = date.today()
    counts, dates = [], []
    for i in range(num_days):
        counts.append(get_create_review_count(username=username, start_date=start_date))
        dates.append(start_date.strftime("%d-%b"))
        start_date = start_date - timedelta(days=1)
    return {
        "title": "Review received",
        "counts": counts,
        "dates": dates,
    }


def get_create_review_count(username: str, start_date: date) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    review_count = ReviewModel.Review.objects.filter(creator=creator, created_on__date=start_date).count()
    return review_count


def get_average_rating(username: str, num_days: int):
    creator = UserDao.get_creator_from_username(username=username)
    end_date = date.today()
    start_date = end_date - timedelta(days=num_days)
    avg_rating = ReviewModel.Review.objects.filter(creator=creator, created_on__range=(start_date, end_date)).aggregate(Avg('ratings'))['ratings__avg']
    return avg_rating or "Oops!! you don't have reviews."


def get_total_number_of_reviews(username: str, num_days: int) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    end_date = date.today()
    start_date = end_date - timedelta(days=num_days)
    return int(ReviewModel.Review.objects.filter(creator=creator, created_on__range=(start_date, end_date)).count())

