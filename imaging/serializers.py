from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from disease.models import Disease
from disease.serializers import DiseaseSerializer
from harrison.common.mixins import DateTimeSerializerMixin
from imaging.models import MedicalImage, ImageLabel


class ImageLabelSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=False,
        help_text="The name of the image"
    )
    disease = DiseaseSerializer(
        many=True,
        required=False,
        help_text="The related diseases"
    )

    def validate(self, attrs):
        if not attrs.get('disease'):
            return super().validate(attrs)

        disease_list = attrs.get('diseases')
        try:
            if not isinstance(disease_list, list):
                disease_list = [disease_list]

            obj_list = [Disease.objects.get(name=item.get('name')) for item in disease_list]
        except Disease.DoesNotExist:
            raise ValidationError('Invalid disease names, please check the input and try again')

        attrs['disease'] = obj_list

        return attrs

    def update(self, instance, validated_data):
        if validated_data.get('disease'):
            instance.disease.clear()
            [instance.disease.add(disease) for disease in validated_data.get('disease')]
            validated_data.pop('disease')

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    def create(self, validated_data):
        obj, _ = ImageLabel.objects.get_or_create(
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
        required=True,
        help_text="The related image"
    )
    label = ImageLabelSerializer(
        many=True,
        required=False,
        help_text="The related labels"
    )

    def validate(self, attrs):
        if not attrs.get('label'):
            return super().validate(attrs)

        try:
            objects = [ImageLabel.objects.get(name=label.get('name')) for label in attrs.get('label')]
        except ImageLabel.DoesNotExist:
            raise ValidationError('You have provided an invalid set of labels, please correct them and try again')

        attrs['label'] = objects

        return attrs

    def update(self, instance, validated_data):
        if validated_data.get('label'):
            instance.label.clear()
            [instance.label.add(label) for label in validated_data.get('label')]
            validated_data.pop('label')

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    def create(self, validated_data):
        user = self.context['request'].user

        obj = MedicalImage.objects.create(
            created_by=user,
            **validated_data
        )

        return obj
