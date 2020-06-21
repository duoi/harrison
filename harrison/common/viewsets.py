from rest_framework import viewsets, mixins


class BaseViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = None
