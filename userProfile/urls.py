from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('profile', login_required(views.ProfileView.as_view()), name='profile'),
]