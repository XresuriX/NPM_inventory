import factory
from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth.models import User
from report import models

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'


class IngredientsFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = models.Ingredients

    id = fake.unique.random_int()
    name = factory.LazyAttribute(lambda _: fake.name())
    discription = fake.text()




