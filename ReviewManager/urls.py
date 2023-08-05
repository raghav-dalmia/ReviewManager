"""
URL configuration for ReviewManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home_page(request):
    if request.user.is_authenticated:
        return redirect('creatorAnalytics', num_days=7)
    return redirect("https://revulink.vercel.app/")


views = [
    # Will have landing page on this route
    path('', home_page, name='home'),
    path('form/', login_required(TemplateView.as_view(template_name='./components/form.html')), name='form'),
    path('home_error/', TemplateView.as_view(template_name='./components/error.html'), name="home_error"),
    path('400/', TemplateView.as_view(template_name='./components/error.html'), name='error_400'),
    path('500/', TemplateView.as_view(template_name='./components/error.html'), name='error_500'),
    path('terms/condition', TemplateView.as_view(template_name='./tnc.html'), name="tnc"),
]

urlpatterns = views + [
    path('admin/', admin.site.urls),
    path('auth/', include('appAuth.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('userProfile.urls')),
    path('review/', include('reviewService.urls')),
    path('', include('creatorPage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
