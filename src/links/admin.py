from django.contrib import admin

from links.models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Link._meta.get_fields()[:-1]]
    readonly_fields = (
        "id",
        "owner",
        "dt",
        "tags",
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    readonly_fields = (
        "id",
        "links_string",
    )


admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
