from imaging.models import MedicalImage


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

    def create(self, validated_data):
        user = None  # pass user back
        obj = MedicalImage.objects.create(
            created_by=user
            **validated_data
        )

        return obj
