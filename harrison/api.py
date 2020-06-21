
from django.urls import include, path
from rest_framework import routers

from imaging.viewsets import MedicalImageViewSet, ImageLabelViewSet

router = routers.SimpleRouter()
router.register(r'imaging', MedicalImageViewSet)
router.register(r'labels', ImageLabelViewSet)

urlpatterns = [
    path(r'api/v1/', include((router.urls, 'router'), namespace='v1'))
]
