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
from django.conf import settings
from django.contrib.auth.decorators import login_required

views = [
    # Will have landing page on this route
    path('', login_required(TemplateView.as_view(template_name='./components/profile.html')), name='home'),
    path('form/', login_required(TemplateView.as_view(template_name='./components/form.html')), name='form'),
]

urlpatterns = views + [
    path('admin/', admin.site.urls),
    path('auth/', include('appAuth.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('userProfile.urls')),
    path('review/', include('reviewService.urls')),
    path('', include('creatorPage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
