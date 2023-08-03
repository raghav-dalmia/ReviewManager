from datetime import timedelta
from django.db.models import Sum
from django.utils import timezone
from pytz import timezone as pytz_timezone
from .models import PageView

current_timezone = pytz_timezone('Asia/Kolkata')


def add_view_review_analytics(creator):
    page_visit, created = PageView.objects.get_or_create(date=timezone.now().astimezone(current_timezone).date(), creator=creator)
    page_visit.visit_count += 1
    page_visit.save()


def get_review_page_view_context(request, num_days: int) -> dict:
    start_date = timezone.now().astimezone(current_timezone).date()
    counts, dates, total_view = [], [], 0
    for i in range(num_days):
        count = get_view_review_count(request=request, start_date=start_date)
        counts.append(count)
        total_view += count
        dates.append(start_date.strftime("%d-%b"))
        start_date = start_date - timedelta(1)
    return {
        "title": "Views on RevuLink",
        "counts": counts[::-1],
        "dates": dates[::-1],
        "total_views": total_view,
    }


def get_view_review_count(request, start_date) -> int:
    creator = request.creator
    page_view, created = PageView.objects.get_or_create(creator=creator, date=start_date)
    return page_view.visit_count or 0

