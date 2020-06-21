import random, factory, faker
from django.contrib.auth import get_user_model

from classification.models import ClassificationCode, ClassificationStandard


class ClassificationCodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassificationCode

    identifier = factory.Sequence(lambda n: 'CC-%06d' % n)
    description = factory.Faker('company')

    @factory.lazy_attribute
    def standard(self):
        return random.choice(ClassificationStandard.objects.all())
