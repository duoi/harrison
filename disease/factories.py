import random, factory

from classification.factories import ClassificationCodeFactory
from disease.models import Disease
from harrison.common.factories import UserFactory


class RandomDiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Disease

    created_by = factory.SubFactory(UserFactory)
    name = factory.Faker('company')

    @factory.lazy_attribute
    def snomed_ct_reference(self):
        if not random.randint(0,2) == 0:
            return

        return ClassificationCodeFactory()

    @factory.lazy_attribute
    def icd_10_reference(self):
        if not random.randint(0, 2) == 0:
            return

        return ClassificationCodeFactory()

    @factory.lazy_attribute
    def icd_9_reference(self):
        if not random.randint(0, 2) == 0:
            return

        return ClassificationCodeFactory()
