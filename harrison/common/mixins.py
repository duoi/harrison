from django.db import models
from django.utils.timezone import now


class DateTimeMixin(models.Model):
    date_created = models.DateTimeField(
        default=now(),
        editable=False
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )
