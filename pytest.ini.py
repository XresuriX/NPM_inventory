import pytest

from npm_inventory import settings


[pytest]
DJANGO_SETTINGS_MODULE= npm_inventory.settings


python_files = test_*.py

markers =
    slow: slow running test