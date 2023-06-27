from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter

from coolmarks.views import status_view
from core.views import UserViewSet, LinkViewSet, TagViewSet


router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, "user")
router.register("links", LinkViewSet, "link")
router.register("tags", TagViewSet, "tag")

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("status/", status_view, name="status"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", authtoken_views.obtain_auth_token),
    path("auth/", include("allauth.urls")),
    path("_/vip/", admin.site.urls),
]
