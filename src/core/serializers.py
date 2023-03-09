from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Link, Tag


class CustomSerializer(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        field_names += getattr(self.Meta, "extra_fields", type(field_names)())
        return field_names


class UserSerializer(CustomSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
        ]
        extra_fields = [
            "link_set",
        ]


class LinkSerializer(CustomSerializer):
    class Meta:
        model = Link
        fields = "__all__"
        extra_fields = [
            "id",
        ]

    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        if (tag_list := data.get("tag_list")) is not None:
            value["tags"] = Tag.from_list(tag_list)
        return value


class TagSerializer(CustomSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
