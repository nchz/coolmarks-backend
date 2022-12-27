"""
GET /links/
POST /links/
POST /links/delete/
POST /links/edit/
POST /links/update/

body = {
    # for delete, edit and update.
    "link_ids": <list of ints>,
    # only for update.
    "action": <"add", "remove" or "set">,
    "_tags_string": <str>
}
"""
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from links.models import Link, Tag


@login_required
@require_http_methods(["GET", "POST"])
def list_view(request):
    """
    List `request.user` links on GET, create a new `Link` on POST.
    """
    if request.method == "GET":
        link_list = Link.objects.filter(owner=request.user).order_by("-dt")
        context = {
            "link_list": link_list,
        }
        return render(request, "links/index.html", context)

    elif request.method == "POST":
        if "location" not in request.POST:
            return HttpResponseBadRequest()

        location = request.POST["location"]
        _tags_string = request.POST.get("_tags_string", "")

        link = Link(
            owner=request.user,
            location=location,
        )
        link._tags_string = _tags_string
        link.save()

        return HttpResponseRedirect(reverse("links:list"))


@login_required
@require_http_methods(["POST"])
def delete_view(request):
    link_ids = [int(i) for i in request.POST.get("link_ids", "").split(",") if i != ""]
    objs = Link.objects.filter(
        pk__in=link_ids,
        owner=request.user,
    )
    objs.delete()
    return HttpResponseRedirect(reverse("links:list"))


@login_required
@require_http_methods(["POST"])
def edit_view(request):
    link_ids = [int(i) for i in request.POST.get("link_ids", "").split(",") if i != ""]
    action = request.POST.get("action")
    _tags_string = request.POST.get("_tags_string", "")

    tags = Tag.from_string(_tags_string)
    if action == "set":
        tags = [tags]

    objs = Link.objects.filter(
        pk__in=link_ids,
        owner=request.user,
    )
    for o in objs:
        getattr(o.tags, action)(*tags)

    return HttpResponseRedirect(reverse("links:list"))


@login_required
@require_http_methods(["GET", "POST"])
def bulk_add_view(request):
    if request.method == "GET":
        return render(request, "links/bulk.html")

    elif request.method == "POST":
        if "location_list" not in request.POST:
            return HttpResponseBadRequest()

        location_list = request.POST["location_list"]
        _tags_string = request.POST.get("_tags_string", "")

        locations = [loc.strip() for loc in location_list.split() if loc.strip()]
        for location in locations:
            parsed_loc = urlparse(location)
            if parsed_loc.scheme and parsed_loc.netloc:
                link = Link(
                    owner=request.user,
                    location=location,
                )
                link._tags_string = _tags_string
                link.save()

        return HttpResponseRedirect(reverse("links:list"))
