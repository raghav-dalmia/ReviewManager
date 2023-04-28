from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('form/<str:username>/', views.ReviewFormView.as_view(), name="reviewForm"),
]