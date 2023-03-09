import re
from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.db import models


MAX_LENGTH = 200


class Tag(models.Model):
    # TODO unique=True,
    # TODO Use models.SlugField
    name = models.CharField(
        max_length=MAX_LENGTH,
    )

    @classmethod
    def from_list(cls, tag_list):
        """
        Return a list of Tag instances whose names come from `tag_list`.
        """
        tags = set()
        for t in tag_list:
            if (tag := cls._clean_tag(t)) != "":
                tags.add(tag)
        return [cls.objects.get_or_create(name=t)[0] for t in tags]

    @staticmethod
    def _clean_tag(tag):
        # NOTE: Keep consistent with frontend!
        tag = re.sub(r"[\s|\-|_]+", "_", tag)
        tag = re.sub(r"\W", "", tag)
        tag = re.sub(r"_+", "_", tag).strip("_")
        tag = tag.replace("_", "-").lower()
        return tag[:MAX_LENGTH]

    def __str__(self):
        return f"[{self.id}] {self.name}"

    def links_string(self):
        return "\n".join(str(link) for link in self.link_set.all())


class Link(models.Model):
    # Relationships
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
    )
    # Fields
    dt = models.DateTimeField(
        auto_now_add=True,
    )
    # NOTE: Underlying URLValidator allows only http(s) and ftp(s).
    location = models.URLField()
    domain = models.CharField(
        max_length=MAX_LENGTH,
        editable=False,
    )
    title = models.CharField(
        max_length=MAX_LENGTH,
        blank=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )
    # TODO
    # description = models.TextField(
    #     editable=False,
    # )

    class Meta:
        # TODO
        # unique_together = ["owner", "location"]
        ordering = ["-dt"]

    def save(self, *args, **kwargs):
        self.domain = urlparse(self.location).netloc[:MAX_LENGTH]
        self.title = (self.title or self.location)[:MAX_LENGTH]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.id}; {self.owner.username}] {self.location} :: {self.title}"
