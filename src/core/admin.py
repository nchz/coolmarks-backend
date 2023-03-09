from django.contrib import admin

from core.models import Link, Tag


class LinkTagsInline(admin.TabularInline):
    model = Link.tags.through


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Link._meta.get_fields()[:-1]]
    readonly_fields = [
        "dt",
        "id",
        "owner",
        "tags",
    ]
    inlines = [
        LinkTagsInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        LinkTagsInline,
    ]
