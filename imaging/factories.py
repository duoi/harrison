import random, factory

from disease.factories import RandomDiseaseFactory
from harrison.common.factories import UserFactory
from imaging.models import MedicalImage, ImageLabel


class ImageLabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageLabel

    created_by = factory.SubFactory(UserFactory)
    name = factory.Faker('company')

    @factory.post_generation
    def groups(self, create, *args, **kwargs):
        if not create:
            return

        disease_list = [RandomDiseaseFactory() for i in range(random.randint(1,3))]
        for disease in disease_list:
            self.disease.add(disease)


class MedicalImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicalImage

    created_by = factory.SubFactory(UserFactory)
    image = factory.django.ImageField()

    @factory.post_generation
    def label(self, *args, **kwargs):
        label_list = [ImageLabelFactory() for i in range(random.randint(1,3))]
        for label in label_list:
            self.label.add(label)

        return self.label
