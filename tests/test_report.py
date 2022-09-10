import pytest
from django.contrib.auth.models import User
from .factories import IngredientsFactory


"""@pytest.fixture()
def user_1(db):
   return User.objects.create_user("test-user")"""


"""@pytest.mark.django_db
def test_new_user_1(user_factory):
    we can use either .create() or .build()
    to make a new user the difference is one user will be saved to the db
    user = user_factory.build()
    count = User.objects.all().count
    print(count)"""

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True


"""def test_set_check_password1(user_1):
    print('check-user1')
    assert user_1.username == "test-user"


def test_set_check_password2(user_1):
    print('check-user2')
    assert user_1.username == "test-user"
"""

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "MyName"


"""def test_new_user(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff"""


def test_new_user(new_user_1):
    print(new_user_1.username)
    assert True


def test_new_product(db, ingredients):
    print(ingredients.discription)
    assert True

