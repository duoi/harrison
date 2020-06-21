from django.db import IntegrityError
from django.test import TestCase

from classification.factories import (
    SnomedClassificationCodeFactory,
    ICD10ClassificationCodeFactory,
    ICD9ClassificationCodeFactory,
)
from disease.factories import RandomDiseaseFactory


class DiseaseTest(TestCase):
    def test_string_representation(self):
        obj = RandomDiseaseFactory()

        assert str(obj) == obj.name

    def test_can_create_model_with_all_attributes(self):
        snomed = SnomedClassificationCodeFactory()
        icd_10 = ICD10ClassificationCodeFactory()
        icd_9 = ICD9ClassificationCodeFactory()

        obj = RandomDiseaseFactory(
            snomed_ct_reference=snomed,
            icd_10_reference=icd_10,
            icd_9_reference=icd_9
        )

        assert obj.snomed_ct_reference == snomed
        assert obj.icd_9_reference == icd_9
        assert obj.icd_10_reference == icd_10

    def test_can_create_model_without_codes(self):
        obj = RandomDiseaseFactory(
            snomed_ct_reference=None,
            icd_10_reference=None,
            icd_9_reference=None
        )

        assert obj.id

    def test_not_having_created_by_raises_exception(self):
        self.assertRaises(IntegrityError, lambda: RandomDiseaseFactory(created_by=None))
