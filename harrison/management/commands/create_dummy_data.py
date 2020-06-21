import random

from django.core.management.base import BaseCommand

from harrison.common.factories import DoctorUserFactory, ResearcherUserFactory
from imaging.factories import MedicalImageFactory
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Create dummy data'

    def handle(self, *args, **options):
        print('--- Creating populated doctors (all passwords are \'aaa\' without quotation marks)')
        print('--- Doctor credentials')

        for round in range(3):
            doctor = DoctorUserFactory(is_staff=True)
            [MedicalImageFactory(created_by=doctor) for i in range(random.randint(3,10))]
            doctor.set_password('aaa')
            doctor.save()
            token = Token.objects.create(user=doctor)
            print(f'Username {round}: {doctor.username}')
            print(f'Token {round}: {token}')

        print('--- Creating unpopulated users (all passwords are \'aaa\' without quotation marks)')
        print('--- Doctor credentials')
        for round in range(3):
            doctor = DoctorUserFactory(is_staff=True)
            doctor.set_password('aaa')
            doctor.save()
            token = Token.objects.create(user=doctor)

            print(f'Username {round}: {doctor.username}')
            print(f'Token {round}: {token}')

        print('--- Researcher credentials')
        for round in range(3):
            user = ResearcherUserFactory(is_staff=True)
            user.set_password('aaa')
            user.save()
            token = Token.objects.create(user=user)

            print(f'Username {round}: {user.username}')
            print(f'Token {round}: {token}')

        print('Use /admin to auth')
