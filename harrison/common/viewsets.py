from rest_framework import viewsets, mixins, permissions, authentication


class BaseViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
    ):
    serializer_class = None

    authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def initialize_request(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
