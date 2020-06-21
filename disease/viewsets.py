from disease.models import Disease
from disease.serializer import DiseaseSerializer
from harrison.common.viewsets import BaseViewSet


class DiseaseViewSet(BaseViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()
