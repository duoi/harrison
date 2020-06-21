from rest_framework import serializers

from classification.models import ClassificationStandard, ClassificationCode
from harrison.common.mixins import DateTimeSerializerMixin


class ClassificationCodeSerializer(DateTimeSerializerMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].choices = ClassificationStandard.objects.all()

    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The primary key of this image"
    )
    identifier = serializers.CharField(
        required=False
    )
    standard = serializers.ChoiceField(
        write_only=True,
        required=True,
        choices=[],
        help_text = "The classification standard"
    )
    description = serializers.CharField(
        required=False
    )

    def create(self, validated_data):
        obj, _ = ClassificationCode.objects.get_or_create(
            **validated_data
        )

        return obj
