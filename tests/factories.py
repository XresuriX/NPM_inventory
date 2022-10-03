import factory
from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth.models import User
from report import models

fake = Faker()


# example
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'


# Factory for the ingredients model
class IngredientsFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = models.Ingredients

    id = fake.unique.random_int()
    name = factory.LazyAttribute(lambda _: fake.name())


# Factory for the report model
class ReportsFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = models.Report

    id = factory.SubFactory(IngredientsFactory)
    name = fake.name()
    opening_bgs = fake.random_int()
    opening_kgs = fake.pyfloat()
    received = fake.random_int()
    bags_used_bin = fake.random_int()
    bags_used_Th3 = fake.random_int()
    kgs_used_Th3 = fake.pyfloat()
    lot_number = fake.pystr_format()
    current_bgs = fake.random_int()
    current_kgs = fake.pyfloat()
    total_used_kgs = fake.random_int()
    expiry_date = fake.date()







