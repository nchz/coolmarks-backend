from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from core.utils import validate_tag_name


MAX_LENGTH = 200


class Tag(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
        validators=[validate_tag_name],
    )

    def __str__(self):
        return f"[{self.id}] {self.name}"


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


# Create Auth Tokens for each newly created user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
