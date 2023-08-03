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
        "num_page_view": creatorPageDao.get_review_page_view_context(request=request, num_days=num_days),
        "num_review_created": reviewServiceDao.get_review_form_view_context(request=request, num_days=num_days)
    }
    context["total_views"] = context.get("num_page_view").get("total_views")
    context["avg_rating"] = context.get("num_review_created").get("avg_rating")
    context["total_reviews"] = context.get("num_review_created").get("total_reviews")
    context["max_range"] = int(
        max(max(context.get("num_page_view").get("counts")), max(context.get("num_review_created").get("counts")))) + 1
    if context["max_range"] % 2 == 1:
        context["max_range"] += 1
    return render(request, 'components/results.html', context)
