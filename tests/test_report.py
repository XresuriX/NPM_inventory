import pytest
from django.contrib.auth.models import User
from .factories import IngredientsFactory, ReportsFactory
from report.models import Report, Ingredients

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
    print(ingredients.description)
    assert True


"""@pytest.mark.django_db
def test_new_report(reports_factory):
    print(reports_factory.id)
    print(reports_factory.name)
    print(reports_factory.opening_bgs)
    print(reports_factory.opening_kgs)
    print(reports_factory.received)
    print(reports_factory.bags_used_bin)
    print(reports_factory.bags_used_Th3)
    print(reports_factory.kgs_used_Th3)
    print(reports_factory.lot_number)
    print(reports_factory.current_bgs)
    print(reports_factory.current_kgs)
    print(reports_factory.total_used_kgs)
    print(reports_factory.expiry_date)
    assert True"""


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, opening_bgs, opening_kgs, received, bags_used_bin, bags_used_Th3, kgs_used_Th3, "
    " current_bgs, current_kgs, total_used_kgs,  validity",
    [
        ("CBtest", 0, 0, 0, 0, 0, 0, 0, 0, 0, True),
        ("CBtest1", 1, 0, 0, 0, 0, 0, 1, 0, 0, True),
        ("CBtest2", 0, 1, 0, 0, 0, 0, 0, 1, 0, True),
        ("CBtest3", 10, 0, 3, 0, 0, 0, 13, 0, 0, True),
        ("CBtest4", 10, 0, 0, 5, 0, 0, 0, 5, 125.00, True),
        ("CBtest5", 0, 0, 24, 0, 0, 0, 10, 0, 250.00, True),
        ("CBtest6", 1, 0, 2, 0, 0, 0, 3, 0, 0, True),
        ("CBtest7", 150, 22.50, 0, 25, 0, 20.50, 125, 2.00, 645.50, True),
        ("CBtest8", 1, 0, 300, 0, 260, 0, 41, 0, 6500, True),
        ("CBtest9", 150, 15.65, 150, 10, 50, 1000, 240, 15.65, 1200, True),
        ("CBtest10", 160, 0, 40, 10, 13, 340, 186, 10.00, 340, True),
    ],
)
def test_report_instance(
        db, reports_factory, name, opening_bgs, opening_kgs, received, bags_used_bin, bags_used_Th3, kgs_used_Th3,
        current_bgs, current_kgs, total_used_kgs, validity
):
    test = reports_factory(
        name=name,
        opening_bgs=opening_bgs,
        opening_kgs=opening_kgs,
        received=received,
        bags_used_bin=bags_used_bin,
        bags_used_Th3=bags_used_Th3,
        kgs_used_Th3=kgs_used_Th3,

        current_bgs=current_bgs,
        current_kgs=current_kgs,
        total_used_kgs=total_used_kgs,

    )

    item = Report.objects.all().count()
    print(item)
    assert item == validity


@pytest.mark.parametrize(
    "name, id, validity",
    [
        ("CBTester1", 1, True),
        ("CBTester2", 2, True),
    ],
)
def test_ingredients_instance(
    db, ingredients_factory, name, id, validity
):

    test = ingredients_factory(
        name=name,
        id=id,
    )

    item = Ingredients.objects.all().count()
    print(item)
    assert item == validity



