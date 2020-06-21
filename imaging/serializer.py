from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from disease.models import Disease
from disease.serializer import DiseaseSerializer
from harrison.common.mixins import DateTimeSerializerMixin
from imaging.models import MedicalImage, ImageLabel


class ImageLabelSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=False
    )
    disease = DiseaseSerializer(
        many=True,
        required=False
    )

    def validate(self, attrs):
        if not attrs.get('disease'):
            return super().validate(attrs)

        disease_list = attrs.get('disease')
        try:
            if not isinstance(disease_list, list):
                disease_list = [disease_list]

            obj_list = [Disease.objects.get(name=item) for item in disease_list]
        except Disease.DoesNotExist:
            raise ValidationError('Invalid disease names, please check the input and try again')

        attrs['disease'] = obj_list

        return attrs

    def create(self, validated_data):
        obj = ImageLabel.objects.get_or_create(
            created_by=self.context['request'].user,
            **validated_data
        )

        if validated_data.get('disease'):
            obj.add(*validated_data.get('disease'))

        return obj



class MedicalImageSerializer(DateTimeSerializerMixin):
    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The primary key of this image"
    )
    createdBy = serializers.CharField(
        read_only=True,
        required=False,
        source="created_by"
    )
    image = serializers.FileField(
        required=True
    )
    labels = ImageLabelSerializer(
        many=True,
        required=False
    )

    def validate(self, attrs):
        if not attrs.get('labels'):
            return super().validate(attrs)

        try:
            objects = [ImageLabel.objects.get(name=label) for label in attrs.get('labels')]
        except ImageLabel.DoesNotExist:
            raise ValidationError('You have provided an invalid set of labels, please correct them and try again')

        attrs['labels'] = objects

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user

        obj = MedicalImage.objects.create(
            created_by=user,
            **validated_data
        )

        return obj
