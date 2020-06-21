from rest_framework import viewsets, mixins, permissions, authentication


class BaseViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
    ):
    serializer_class = None

    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticated]
