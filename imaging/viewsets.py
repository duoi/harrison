from django.views.static import serve

from harrison.common.constants import MEDICAL_DOCTOR_USER_GROUP
from harrison.common.permissions import IsResearcherOrReadOnly, IsDoctorOrReadOnly
from harrison.common.viewsets import BaseViewSet
from imaging.models import MedicalImage, ImageLabel
from imaging.serializers import MedicalImageSerializer, ImageLabelSerializer
from django.contrib.auth.decorators import login_required


class MedicalImageViewSet(BaseViewSet):
    serializer_class = MedicalImageSerializer
    queryset = MedicalImage.objects.all()

    permission_classes = [IsDoctorOrReadOnly,]

    def get_queryset(self):
        if self.request.user.groups.filter(name=MEDICAL_DOCTOR_USER_GROUP).exists():
            return MedicalImage.objects.filter(created_by=self.request.user)

        return MedicalImage.objects.all()


class ImageLabelViewSet(BaseViewSet):
    serializer_class = ImageLabelSerializer
    queryset = ImageLabel.objects.all()

    permission_classes = [IsResearcherOrReadOnly,]


@login_required
def login_required_files(*args, **kwargs):
    return serve(*args, **kwargs)
