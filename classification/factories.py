import random, factory

from classification.models import ClassificationCode, ClassificationStandard


class ClassificationCodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassificationCode

    identifier = factory.Sequence(lambda n: 'CC-%06d' % n)
    description = factory.Faker('company')

    @factory.lazy_attribute
    def standard(self):
        return random.choice(ClassificationStandard.objects.all())


class SnomedClassificationCodeFactory(ClassificationCodeFactory):
    @factory.lazy_attribute
    def standard(self):
        item, _ = ClassificationStandard.objects.get_or_create(
            name='SNOMED-CT'
        )
        return item


class ICD10ClassificationCodeFactory(ClassificationCodeFactory):
    @factory.lazy_attribute
    def standard(self):
        item, _ = ClassificationStandard.objects.get_or_create(
            name='ICD-10'
        )
        return item


class ICD9ClassificationCodeFactory(ClassificationCodeFactory):
    @factory.lazy_attribute
    def standard(self):
        item, _ = ClassificationStandard.objects.get_or_create(
            name='ICD-9'
        )
        return item
