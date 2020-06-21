from django.db import models

from harrison.common.mixins import DateTimeMixin


class Event(DateTimeMixin):
    """
    This is a fairly simple table that seeks to record
    every single interaction with the website.

    It can be extended as needed, naturally.
    """
    user = models.ForeignKey(
        'auth.User',
        editable=False,
        on_delete=models.DO_NOTHING,
        help_text="The user that this event relates to",
        related_name="events",
        null=True,
        blank=True,
        default=None
    )
    url = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text="The url that was requested"
    )
    request_dump = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text="A string dump of the request headers"
    )




