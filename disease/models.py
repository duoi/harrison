from django.db import models
import reversion

from harrison.common.mixins import DateTimeMixin


@reversion.register()
class Disease(DateTimeMixin):
    created_by = models.ForeignKey(
        'auth.User',
        editable=False,
        on_delete=models.DO_NOTHING,
        help_text="The user that created this disease entry"

    )
    name = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text="The name of the disease being referenced",
        unique=True
    )
    snomed_ct_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="snomed_ct_disease",
        help_text="The SNOMED-CT code for this disease"
    )
    icd_10_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="icd_10_disease",
        help_text="The ICD-10 code for this disease"
    )
    icd_9_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="icd_9_disease",
        help_text="The ICD-9 code for this disease"
    )

    def __str__(self):
        return f"{self.name}"
