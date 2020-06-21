from django.db import models
from django.utils.functional import cached_property
from harrison.common.mixins import DateTimeMixin


class ImageLabel(DateTimeMixin):
    created_by = models.ForeignKey(
        'auth.User',
        default=None,
        null=True,
        blank=True,
        editable=False,
        on_delete=models.DO_NOTHING,
        help_text="The user that created this label"
    )
    name = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text="The value of the label"
    )

class MedicalImage(DateTimeMixin):
    created_by = models.ForeignKey(
        'auth.User',
        default=None,
        null=True,
        blank=True,
        editable=False,
        on_delete=models.DO_NOTHING,
        help_text="The user that uploaded this image"
    )
    # This is left as a filefield as I'm unsure of the image format constraints needed
    image = models.FileField(
        help_text="The image that has been uploaded"
    )
    labels = models.ManyToManyField(
        'imaging.MedicalImage',
        related_name="images_using_label",
        help_text="The labels associated with this image"
    )

    @cached_property
    def filetype(self):
        return self.image.file_type
