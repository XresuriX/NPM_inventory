import pytest
from django.contrib.auth.models import User
from .factories import IngredientsFactory, ReportsFactory

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


@pytest.mark.django_db
def test_new_product(ingredients):
    print(ingredients.discription)
    assert True


@pytest.mark.django_db
def test_new_report(reports_factory):
    print(reports_factory.id)
    print(reports_factory.name)
    print(reports_factory.opening_bgs)
    print(reports_factory.opening_kgs)
    print(reports_factory.recieved)
    print(reports_factory.bags_used_bin)
    print(reports_factory.bags_used_Th3)
    print(reports_factory.kgs_used_Th3)
    print(reports_factory.lot_number)
    print(reports_factory.current_bgs)
    print(reports_factory.current_kgs)
    print(reports_factory.total_used_kgs)
    print(reports_factory.expiry_date)
    assert True


@pytest.mark.parametrize(
    "name, opening_bgs, opening_kgs, recieved, bags_used_bin, bags_used_Th3, kgs_used_Th3, "
    " current_bgs, current_kgs, total_used_kgs,  validity",
    [
        ("NewTitle", 0, 0, 0, 0, 0, 0, 0, 0, 0, True),

    ],
)
def test_report_instance(
        db, reports_factory, name, opening_bgs, opening_kgs, recieved, bags_used_bin, bags_used_Th3, kgs_used_Th3,
         current_bgs, current_kgs, total_used_kgs, validity
):
    test = reports_factory(
        name=name,
        opening_bgs=opening_bgs,
        opening_kgs=opening_kgs,
        recieved=recieved,
        bags_used_bin=bags_used_bin,
        bags_used_Th3=bags_used_Th3,
        kgs_used_Th3=kgs_used_Th3,

        current_bgs=current_bgs,
        current_kgs=current_kgs,
        total_used_kgs=total_used_kgs,

    )

    item = ReportsFactory.objects.all().count()
    print(item)
    assert item == validity
