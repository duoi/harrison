from django.db import models

# Create your models here.
from harrison.common.mixins import DateTimeMixin


class ClassificationStandard(DateTimeMixin):
    name = models.TextField(
        help_text="The name of this standard (ICD-10, ICD-9 etc)"
    )

    def __str__(self):
        return self.name


class ClassificationCode(DateTimeMixin):
    identifier = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text='Classification standard\'s code for this condition'
    )
    standard = models.ForeignKey(
        'disease.ClassificationStandard',
        default=None,
        null=True,
        blank=True,
        help_text="The classification standard (ICD-10, SNOMED-CT etc)",
        on_delete=models.DO_NOTHING
    )
    description = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text='The shorthand description for this condition'
    )

    def __str__(self):
        return f"{self.standard} {self.identifier}"
