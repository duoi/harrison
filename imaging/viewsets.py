from harrison.common.permissions import IsResearcherOrReadOnly, IsDoctorOrReadOnly
from harrison.common.viewsets import BaseViewSet
from imaging.models import MedicalImage, ImageLabel
from imaging.serializer import MedicalImageSerializer, ImageLabelSerializer


class MedicalImageViewSet(BaseViewSet):
    serializer_class = MedicalImageSerializer
    queryset = MedicalImage.objects.all()

    permission_classes = [IsDoctorOrReadOnly,]


class ImageLabelViewSet(BaseViewSet):
    serializer_class = ImageLabelSerializer
    queryset = ImageLabel.objects.all()

    permission_classes = [IsResearcherOrReadOnly,]
