from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase, APIRequestFactory

from classification.factories import (
    SnomedClassificationCodeFactory, ICD10ClassificationCodeFactory,
    ICD9ClassificationCodeFactory,
)
from disease.factories import RandomDiseaseFactory
from disease.serializers import DiseaseSerializer
from harrison.common.factories import UserFactory


class DiseaseSerializerTest(APITestCase):
    def create_serializer_and_context(self):
        serializer = DiseaseSerializer()
        serializer.context['request'] = APIRequestFactory()
        serializer.context['request'].user = UserFactory()

        return serializer

    def test_create_method_with_valid_data(self):
        serializer = self.create_serializer_and_context()

        valid_data = {
            'name': 'Some name',
        }

        # test
        obj = serializer.create(valid_data)
        assert obj.created_by == serializer.context['request'].user
        assert obj.name == valid_data.get('name')
        assert obj.snomed_ct_reference == None
        assert obj.icd_10_reference == None
        assert obj.icd_9_reference == None

    def test_update_existing_instance(self):
        instance = RandomDiseaseFactory()
        snomed_ct_reference = SnomedClassificationCodeFactory()
        icd_10_reference = ICD10ClassificationCodeFactory()
        icd_9_reference = ICD9ClassificationCodeFactory()

        serializer = DiseaseSerializer(instance=instance)
        serializer.context['request'] = APIRequestFactory()
        serializer.context['request'].user = UserFactory()

        serializer = self.create_serializer_and_context()

        valid_data = {
            'snomed_ct_reference': snomed_ct_reference,
            'icd_10_reference': icd_10_reference,
            'icd_9_reference': icd_9_reference
        }

        # test
        obj = serializer.update(instance, valid_data)
        assert obj.created_by != serializer.context['request'].user
        assert obj.name == instance.name
        assert obj.id == instance.id
        assert obj.snomed_ct_reference == snomed_ct_reference
        assert obj.icd_10_reference == icd_10_reference
        assert obj.icd_9_reference == icd_9_reference

    def test_validate_without_valid_snomed_ref(self):
        serializer = self.create_serializer_and_context()
        invalid_data = {
            'snomed_ct_reference': 'an-invalid-identifier'
        }
        self.assertRaises(ValidationError, lambda: serializer.validate(invalid_data))

    def test_validate_without_valid_icd_10_ref(self):
        serializer = self.create_serializer_and_context()
        invalid_data = {
            'icd_10_reference': 'an-invalid-identifier'
        }
        self.assertRaises(ValidationError, lambda: serializer.validate(invalid_data))

    def test_validate_without_valid_icd_9_ref(self):
        serializer = self.create_serializer_and_context()
        invalid_data = {
            'icd_9_reference': 'an-invalid-identifier'
        }
        self.assertRaises(ValidationError, lambda: serializer.validate(invalid_data))
