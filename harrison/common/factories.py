import factory, random
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from harrison.common.constants import MEDICAL_DOCTOR_USER_GROUP, RESEARCHER_USER_GROUP


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker('first_name').generate({})
    last_name = factory.Faker('last_name').generate({})
    email = factory.Faker('email').generate({})

    @factory.lazy_attribute
    def username(self):
        def create_username():
            try:
                 username = f"{random.randint(00000, 99999)}@{random.randint(00000, 99999)}.com"
            except:
                 return create_username()
            return username

        return create_username()

class DoctorUserFactory(UserFactory):
    @factory.post_generation
    def add_to_group(self, *args, **kwargs):
        group, _ = Group.objects.get_or_create(
            name=MEDICAL_DOCTOR_USER_GROUP
        )
        group.user_set.add(self)

class ResearcherUserFactory(UserFactory):
    @factory.post_generation
    def add_to_group(self, *args, **kwargs):
        group, _ = Group.objects.get_or_create(
            name=RESEARCHER_USER_GROUP
        )
        group.user_set.add(self)
