from django.db import models
from django.utils.timezone import now
from rest_framework import serializers


class DateTimeMixin(models.Model):
    """
    Reusable mixin that should be inherited on creation of
    any model.
    """
    date_created = models.DateTimeField(
        default=now,
        editable=False
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class DateTimeSerializerMixin(serializers.Serializer):
    dateCreated = serializers.DateTimeField(
        read_only=True,
        required=False,
        source="date_created"
    )
    dateUpdated = serializers.DateTimeField(
        read_only=True,
        required=False,
        source="date_updated"
    )
