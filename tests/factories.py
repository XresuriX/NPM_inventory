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
        model = 'report.Ingredients'

    id = set(fake.unique.random_int() for i in range(100))
    name = factory.LazyAttribute(lambda _: fake.name())
    discription = fake.text()




