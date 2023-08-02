from datetime import date
from django.shortcuts import render
from reviewService import dao as reviewServiceDao
from . import dao as creatorPageDao

userDao = reviewServiceDao.UserDao


def creator_page(request, username: str):
    creator = userDao.get_creator_from_username(username=username)
    creatorPageDao.add_view_review_analytics(creator=creator)
    context = reviewServiceDao.get_review_context(creator=creator)
    context["total_reviews"] = reviewServiceDao.get_overall_number_of_reviews(creator=creator)
    context["avg_rating"] = reviewServiceDao.get_overall_average_rating(creator=creator)
    return render(request, 'creatorPage.html', context)


def creator_analytics(request, num_days: int = 7):
    context = {
        "num_days": num_days,
        "total_views": creatorPageDao.get_total_review_view_count(request=request, num_days=num_days),
        "total_reviews": reviewServiceDao.get_total_number_of_reviews(request=request, num_days=num_days),
        "avg_rating": reviewServiceDao.get_average_rating(request=request, num_days=num_days),
        "num_page_view": creatorPageDao.get_review_page_view_context(request=request, num_days=num_days),
        "num_review_created": reviewServiceDao.get_review_form_view_context(request=request, num_days=num_days)
    }
    context["max_range"] = int(max(max(context.get("num_page_view").get("counts")), max(context.get("num_review_created").get("counts"))))+1
    return render(request, 'components/results.html', context)
