import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_thirdprint():

    msg = "Hello"

    assert msg == "Hi"


@pytest.mark.xfail
def test_fourthprint():

    msg = "Hello"

    assert msg == "Hello"