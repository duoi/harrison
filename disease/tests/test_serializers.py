from django.test import RequestFactory
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase, APIRequestFactory

from disease.serializer import DiseaseSerializer
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
