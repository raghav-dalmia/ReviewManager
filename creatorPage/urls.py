from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('results/<int:num_days>/', login_required(views.creator_analytics), name="creatorAnalytics"),
    path('<str:username>/review/', lambda request, username: redirect('reviewForm', username=username), name='review_form'),
    path('<str:username>/', views.creator_page, name='creatorPage'),
]
