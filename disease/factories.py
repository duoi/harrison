import random, factory

from classification.factories import (
    ICD9ClassificationCodeFactory,
    ICD10ClassificationCodeFactory,
    SnomedClassificationCodeFactory,
)
from disease.models import Disease
from harrison.common.factories import UserFactory


class RandomDiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Disease

    created_by = factory.SubFactory(UserFactory)

    @factory.lazy_attribute
    def name(self, *args, **kwargs):
        return factory.Faker('company').generate({}) + f"{random.randint(00000,99999)}"

    @factory.lazy_attribute
    def snomed_ct_reference(self):
        if not random.randint(0,2) == 0:
            return

        return SnomedClassificationCodeFactory()

    @factory.lazy_attribute
    def icd_10_reference(self):
        if not random.randint(0, 2) == 0:
            return

        return ICD10ClassificationCodeFactory()

    @factory.lazy_attribute
    def icd_9_reference(self):
        if not random.randint(0, 2) == 0:
            return

        return ICD9ClassificationCodeFactory()
