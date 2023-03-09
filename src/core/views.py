from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from core.serializers import UserSerializer, LinkSerializer, TagSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserSerializer.Meta.model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        model = TagSerializer.Meta.model
        return model.objects.filter(link__owner=self.request.user).distinct()


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.link_set.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=["POST"], detail=False)
    def check(self, request):
        """
        Look for the requested `location` in the user's links. Return a list
        with at most one element, the representation of the (found) link.
        """
        location = request.data.get("location")
        links = self.get_queryset().filter(location=location)
        links = self.get_serializer(links, many=True)
        return Response(links.data)
