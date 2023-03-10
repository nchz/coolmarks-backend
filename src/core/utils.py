import re

from django.core.exceptions import ValidationError


def clean_tag_name(tag):
    # NOTE: Keep consistent with frontend!
    tag = re.sub(r"[\s|\-|_]+", "_", tag)
    tag = re.sub(r"\W", "", tag)
    tag = re.sub(r"_+", "_", tag).strip("_")
    tag = tag.replace("_", "-").lower()
    return tag


def validate_tag_name(value):
    if clean_tag_name(value) != value:
        raise ValidationError(f"Tag name '{value}' contains invalid characters.")
