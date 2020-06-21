from rest_framework import serializers

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
    image = serializers.FileField(
        required=True
    )

    def create(self, validated_data):
        user = None  # pass user back
        obj = Disease.objects.create(
            created_by=user
            **validated_data
        )

        return obj
