from django.contrib.auth.models import Group
from rest_framework import permissions

from harrison.common.constants import RESEARCHER_USER_GROUP, MEDICAL_DOCTOR_USER_GROUP


class IsDoctorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.

    Ref: https://www.django-rest-framework.org/api-guide/permissions/#examples
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        import pdb; pdb.set_trace()


        return request.user.groups.filter(
            name=MEDICAL_DOCTOR_USER_GROUP
        ).exists()


class IsResearcherOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.

    Ref: https://www.django-rest-framework.org/api-guide/permissions/#examples
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        import pdb; pdb.set_trace()

        return request.user.groups.filter(
            name=RESEARCHER_USER_GROUP
        ).exists()
