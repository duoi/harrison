from classification.models import ClassificationCode
from classification.serializers import ClassificationCodeSerializer
from harrison.common.permissions import IsResearcherOrReadOnly
from harrison.common.viewsets import BaseViewSet


class ClassificationViewSet(BaseViewSet):
    serializer_class = ClassificationCodeSerializer
    queryset = ClassificationCode.objects.all()

    permission_classes = [IsResearcherOrReadOnly,]

