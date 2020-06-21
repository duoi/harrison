import random

from django.core.management.base import BaseCommand

from harrison.common.factories import DoctorUserFactory, ResearcherUserFactory
from imaging.factories import MedicalImageFactory


class Command(BaseCommand):
    help = 'Create dummy data'

    def handle(self, *args, **options):
        random_range = range(random.randint(10,30))
        [MedicalImageFactory() for round in random_range]

        print('--- Creating users (all passwords are \'a\' without quotation marks)')
        print('--- Doctor credentials')
        for round in range(3):
            doctor = DoctorUserFactory()
            doctor.set_password('aaa')

            print(f'Username {round}: {doctor.username}')

        print('--- Researcher credentials')
        for round in range(3):
            user = ResearcherUserFactory()
            user.set_password('aaa')

            print(f'Username {round}: {user.username}')

        print('Use /admin to auth')
