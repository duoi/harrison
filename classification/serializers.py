from rest_framework import serializers

from harrison.common.mixins import DateTimeSerializerMixin


class ClassificationCodeSerializer(DateTimeSerializerMixin):
    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The primary key of this image"
    )
    identifier = serializers.CharField(
        required=False
    )
    standard = serializers.CharField(
        required=False
    )
    description = serializers.CharField(
        required=False
    )
