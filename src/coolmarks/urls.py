from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("links/", include("links.urls")),
    path("auth/", include("allauth.urls")),
    path("_/vip/", admin.site.urls),
]
