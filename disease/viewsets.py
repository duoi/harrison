from disease.models import Disease
from disease.serializers import DiseaseSerializer
from harrison.common.permissions import IsResearcherOrReadOnly
from harrison.common.viewsets import BaseViewSet


class DiseaseViewSet(BaseViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()

    permission_classes = [IsResearcherOrReadOnly,]
