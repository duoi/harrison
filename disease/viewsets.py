from rest_framework import mixins, viewsets

from imaging.models import MedicalImage


class BaseViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = None


class MedicalImageViewSet(BaseViewSet):
    serializer_class = MedicalImageSerializer
    queryset = MedicalImage.objects.all()
