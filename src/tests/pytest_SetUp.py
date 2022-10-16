import pytest  # TODO: read https://docs.pytest.org/en/6.2.x/fixture.html
from src import corgiweb as corgi
import logging

_SetUp = corgi.SetUp("Tony")
LOGGER = logging.getLogger(__name__)


def test_should_return_1():
    assert _SetUp.get_num_1() == 1

def test_name_should_be_tony():
    assert _SetUp.name == "Tony"