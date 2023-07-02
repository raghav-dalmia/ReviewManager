from datetime import date, timedelta
from django.utils import timezone
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
    review_context = []
    for review in reviews:
        review_img = ReviewModel.ReviewImage.objects.filter(review=review)
        review_context.append({
            "review": review,
            "review_img": review_img
        })
    return {
        "creatorDetail": creator,
        "reviews": review_context
    }


def get_review_form_view_context(username: str, num_days: int) -> dict:
    start_date = timezone.now().date()
    counts, dates = [], []
    for i in range(num_days):
        counts.append(get_create_review_count(username=username, start_date=start_date))
        dates.append(start_date.strftime("%d-%b"))
        start_date = start_date - timedelta(days=1)
    return {
        "title": "Review received",
        "counts": counts[::-1],
        "dates": dates[::-1],
    }


def get_create_review_count(username: str, start_date: date) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    review_count = ReviewModel.Review.objects.filter(creator=creator, created_on__date=start_date).count()
    return review_count


def get_average_rating(username: str, num_days: int):
    creator = UserDao.get_creator_from_username(username=username)
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=num_days-1)
    avg_rating = ReviewModel.Review.objects.filter(creator=creator, created_on__range=(start_date, end_date)).aggregate(Avg('ratings'))['ratings__avg']
    return avg_rating or -1


def get_overall_average_rating(username: str) -> float:
    creator = UserDao.get_creator_from_username(username=username)
    avg_rating = ReviewModel.Review.objects.filter(creator=creator).aggregate(Avg('ratings'))['ratings__avg']
    return avg_rating or 0.0


def get_total_number_of_reviews(username: str, num_days: int) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=num_days - 1)
    return int(ReviewModel.Review.objects.filter(creator=creator, created_on__range=(start_date, end_date)).count())


def get_overall_number_of_reviews(username: str) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    return int(ReviewModel.Review.objects.filter(creator=creator).count())
