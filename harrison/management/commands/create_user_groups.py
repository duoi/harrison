from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from harrison.common import constants

class Command(BaseCommand):
    help = 'Add user groups'

    def handle(self, *args, **options):
        user_groups = [
            constants.HAI_STAFF_USER_GROUP,
            constants.MEDICAL_DOCTOR_USER_GROUP,
            constants.RESEARCHER_USER_GROUP
        ]

        for group in user_groups:
            obj, created = Group.objects.get_or_create(name=group)
            if created:
                print(f'Created user group: "{obj}"')
