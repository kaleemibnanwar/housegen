"""
URL configuration for housegen project.

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
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from core.views import *

urlpatterns = [
    path("admin", admin.site.urls),
    path("", index_view, name="home"),
    path("new", new_project_view, name="new_project"),
    path("project/<project_id>", project_view, name="project_detail"),
    path("pricing", pricing_view, name="pricing"),
    path("login", login_view, name="login"),
    path("sign-up", sign_up_view, name="sign_up"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
