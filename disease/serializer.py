from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from classification.models import ClassificationCode
from disease.models import Disease
from harrison.common.mixins import DateTimeSerializerMixin


class DiseaseSerializer(DateTimeSerializerMixin):
    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The primary key of this image"
    )
    name = serializers.CharField(
        required=True
    )
    snomedCtReference = serializers.CharField(
        required=False,
        source='snomed_ct_reference'
    )
    ICD10Reference = serializers.CharField(
        required=False,
        source='icd_10_reference'
    )
    ICD9Reference = serializers.CharField(
        required=False,
        source='icd_9_reference'
    )
    createdBy = serializers.CharField(
        read_only=True,
        required=False,
        source="created_by"
    )

    def validate(self, attrs):
        """
        This can probably be made smaller by putting the field names
        into a list and iterating over them, passing f strings as
        needed.

        :param attrs:
        :return:
        """
        if attrs.get('snomed_ct_reference'):
            try:
                obj = ClassificationCode.objects.get(
                    standard__name='snomed-ct',
                    identifier=attrs.get('snomed_ct_reference')
                )
            except:
                raise ValidationError('Invalid SNOMED-CT identifier selected')

            attrs['snomed_ct_reference'] = obj

        if attrs.get('icd_10_reference'):
            try:
                obj = ClassificationCode.objects.get(
                    standard__name='icd-10',
                    identifier=attrs.get('icd_10_reference')
                )
            except:
                raise ValidationError('Invalid ICD-10 identifier selected')

            attrs['icd_10_reference'] = obj

        if attrs.get('icd_9_reference'):
            try:
                obj = ClassificationCode.objects.get(
                    standard__name='icd-9',
                    identifier=attrs.get('icd_9_reference')
                )
            except:
                raise ValidationError('Invalid ICD-9 identifier selected')

            attrs['icd_9_reference'] = obj

        return attrs

    def create(self, validated_data):
        user = None  # pass user back
        obj = Disease.objects.create(
            created_by=user
            **validated_data
        )

        return obj
