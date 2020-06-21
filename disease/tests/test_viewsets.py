import random

from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APITestCase, APIRequestFactory

from disease.factories import RandomDiseaseFactory
from disease.viewsets import DiseaseViewSet


class DiseaseViewSetTest(APITestCase):
    request_factory = APIRequestFactory()

    def create_disease_items(self):
        random_range = random.randint(3,10)
        [RandomDiseaseFactory() for i in range(random_range)]

        return random_range

    def test_get_queryset_for_doctor_user(self):
        random_range = self.create_disease_items()

        request = self.request_factory.get('')
        request.user = AnonymousUser

        viewset = DiseaseViewSet()

        setattr(viewset, 'request', request)
        queryset = viewset.get_queryset()

        assert len(queryset) == random_range

    def test_unauthed_user_cannot_view_list(self):
        request = self.request_factory.get('/whatever')
        view = DiseaseViewSet.as_view(actions={'get': 'list'})
        response = view(request)

        # test
        assert response.status_code in (401, 403)
