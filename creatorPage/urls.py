from django.urls import path
from django.shortcuts import redirect
from . import views as CreatorPageView
from django.contrib.auth.decorators import login_required
from reviewService import views as ReviewServiceView

urlpatterns = [
    path('results/<int:num_days>/', login_required(CreatorPageView.creator_analytics), name="creatorAnalytics"),
    path('<str:username>/review/', ReviewServiceView.ReviewFormView.as_view(), name='review_form'),
    path('<str:username>/', CreatorPageView.creator_page, name='creatorPage'),
]
