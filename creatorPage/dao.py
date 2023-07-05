from datetime import timedelta
from django.db.models import Sum
from django.utils import timezone
from pytz import timezone as pytz_timezone
from .models import PageView
from userProfile import dao as UserDao

current_timezone = pytz_timezone('Asia/Kolkata')


def add_view_review_analytics(username: str):
    creator = UserDao.get_creator_from_username(username=username)
    page_visit, created = PageView.objects.get_or_create(date=timezone.now().astimezone(current_timezone).date(), creator=creator)
    page_visit.visit_count += 1
    page_visit.save()


def get_review_page_view_context(username: str, num_days: int) -> dict:
    start_date = timezone.now().astimezone(current_timezone).date()
    counts, dates = [], []
    for i in range(num_days):
        counts.append(get_view_review_count(username=username, start_date=start_date))
        dates.append(start_date.strftime("%d-%b"))
        start_date = start_date - timedelta(1)
    return {
        "title": "Views on review page",
        "counts": counts[::-1],
        "dates": dates[::-1],
    }


def get_view_review_count(username: str, start_date) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    page_view, created = PageView.objects.get_or_create(creator=creator, date=start_date)
    return page_view.visit_count or 0


def get_total_review_view_count(username: str, num_days: int) -> int:
    creator = UserDao.get_creator_from_username(username=username)
    end_date = timezone.now().astimezone(current_timezone).date()
    start_date = end_date - timedelta(days=num_days-1)
    val = PageView.objects.filter(creator=creator, date__range=(start_date, end_date)).aggregate(Sum('visit_count'))['visit_count__sum'] or 0
    return int(val)
