from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup_user, name="signup"),
    path('logout/', login_required(views.logout_user), name="logout"),
]