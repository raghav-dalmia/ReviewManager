from datetime import date, timedelta
from typing import List

from django.utils import timezone
from pytz import timezone as pytz_timezone
from django.db.models import Avg, Sum
from . import models as ReviewModel
from userProfile import dao as UserDao

current_timezone = pytz_timezone('Asia/Kolkata')


def get_review_question(username: str) -> str:
    creator = UserDao.get_creator_from_username(username=username)
    return str(creator.question)


def create_review(feedback: str, reviewee: str, packaging: str, ratings: int, username: str, attachments) -> ReviewModel:
    creator = UserDao.get_creator_from_username(username=username)
    review = ReviewModel.Review.objects.create(creator=creator, feedback=feedback, reviewee=reviewee,
                                               packaging=packaging, ratings=ratings)
    for attachment in attachments:
        ReviewModel.ReviewImage.objects.create(review=review, attachment=attachment)
    return review


def get_review_context(creator) -> dict:
    reviews = ReviewModel.Review.objects.filter(creator=creator, is_deleted=False).order_by(creator.get_orderby_clause())[:creator.resultsToDisplay]
    review_context = []
    for review in reviews:
        review_img = ReviewModel.ReviewImage.objects.filter(review=review, is_deleted=False)
        review_context.append({
            "review": review,
            "review_img": review_img
        })
    return {
        "creatorDetail": creator,
        "reviews": review_context
    }


def get_review_form_view_context(request, num_days: int) -> dict:
    start_date = timezone.now().astimezone(current_timezone).date()
    counts, dates, rating, total_review = [], [], 0.0, 0
    for i in range(num_days):
        count, rate = get_create_review_count(request=request, start_date=start_date)
        counts.append(count)
        rating += rate
        total_review += count
        dates.append(start_date.strftime("%d-%b"))
        start_date = start_date - timedelta(days=1)
    return {
        "title": "Reviews Received",
        "counts": counts[::-1],
        "dates": dates[::-1],
        "total_reviews": total_review,
        "avg_rating": rating / total_review if total_review != 0 else -1,
    }


def get_create_review_count(request, start_date: date) -> List[int]:
    creator = request.creator
    reviews = ReviewModel.Review.objects.filter(creator=creator, created_on__date=start_date, is_deleted=False)
    review_count = reviews.count()
    return [int(review_count or 0), int(reviews.aggregate(Sum('ratings'))['ratings__sum'] or 0)]


def get_average_rating(request, num_days: int):
    creator = request.creator
    end_date = timezone.now().astimezone(current_timezone).date()
    start_date = end_date - timedelta(days=num_days)
    avg_rating = ReviewModel.Review.objects.filter(creator=creator, is_deleted=False, created_on__range=(start_date, end_date)).aggregate(Avg('ratings'))['ratings__avg']
    print(ReviewModel.Review.objects.filter(creator=creator, is_deleted=False, created_on__range=(start_date, end_date)))
    return avg_rating or -1


def get_overall_average_rating(creator) -> float:
    avg_rating = ReviewModel.Review.objects.filter(creator=creator, is_deleted=False).aggregate(Avg('ratings'))['ratings__avg']
    return avg_rating or 0.0


def get_total_number_of_reviews(request, num_days: int) -> int:
    creator = request.creator
    end_date = timezone.now().astimezone(current_timezone).date()
    start_date = end_date - timedelta(days=num_days)
    val = ReviewModel.Review.objects.filter(creator=creator, is_deleted=False, created_on__range=(start_date, end_date)).count() or 0
    return int(val)


def get_overall_number_of_reviews(creator) -> int:
    val = ReviewModel.Review.objects.filter(creator=creator, is_deleted=False).count() or 0
    return int(val)
