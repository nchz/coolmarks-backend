from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Link, Tag
from core.utils import validate_tag_name, get_title_for_url


class TagSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            validate_tag_name(data)
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except (TypeError, ValueError):
            self.fail("invalid")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "link_set",
        ]


class LinkSerializer(serializers.ModelSerializer):
    # Since `Tag.name` is unique, using `TagSerializer(many=True)` here is complicated.
    tags = TagSlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Link
        fields = "__all__"

    def create(self, validated_data):
        if not validated_data.get("title"):
            validated_data["title"] = get_title_for_url(validated_data["location"])

        return super().create(validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
