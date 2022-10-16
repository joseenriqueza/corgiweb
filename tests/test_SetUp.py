# TODO: read https://docs.pytest.org/en/6.2.x/fixture.html
# TODO: read https://stackoverflow.com/questions/37353960/pytest-exits-with-no-error-but-with-collected-0-items


import corgiweb as corgi

_Start = corgi.Start("Tony")

def test_should_return_1():
    assert _Start.get_num_1() == 1
def test_name_should_be_tony():
    assert _Start.name == "Tony"