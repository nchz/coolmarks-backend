from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response

from coolmarks import settings


@api_view()
@ensure_csrf_cookie
def status_view(request):
    return Response(
        {
            "debug": settings.DEBUG,
            "authenticated": request.user.is_authenticated,
        }
    )
