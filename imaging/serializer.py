from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from harrison.common.mixins import DateTimeSerializerMixin
from imaging.models import MedicalImage, ImageLabel


class ImageLabelSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=False
    )


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
        user = None  # pass user back
        obj = MedicalImage.objects.create(
            created_by=user
            **validated_data
        )

        return obj
