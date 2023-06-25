from datetime import date
from django.shortcuts import render
from reviewService import dao as reviewServiceDao
from . import dao as creatorPageDao


def creator_page(request, username: str):
    creatorPageDao.add_view_review_analytics(username=username)
    context = reviewServiceDao.get_review_context(username=username)
    return render(request, 'creatorPage/index.html', context)


def creator_analytics(request, num_days: int = 7):
    username = request.user.username
    context = {
        "num_days": num_days,
        "total_views": creatorPageDao.get_total_review_view_count(username=username, num_days=num_days),
        "total_reviews": reviewServiceDao.get_total_number_of_reviews(username=username, num_days=num_days),
        "avg_rating": reviewServiceDao.get_average_rating(username=username, num_days=num_days),
        "num_page_view": creatorPageDao.get_review_page_view_context(username=username, num_days=num_days),
        "num_review_created": reviewServiceDao.get_review_form_view_context(username=username, num_days=num_days)
    }
    return render(request, 'components/results.html', context)
