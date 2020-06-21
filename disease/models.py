from django.db import models

# Create your models here.
from harrison.common.mixins import DateTimeMixin


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
        help_text="The name of the disease being referenced"
    )
    snomed_ct_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        help_text="The SNOMED-CT code for this disease"
    )
    icd_10_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        help_text="The ICD-10 code for this disease"
    )
    icd_9_reference = models.ForeignKey(
        'classification.ClassificationCode',
        default=None,
        null=True,
        blank=True,
        help_text="The ICD-9 code for this disease"
    )
