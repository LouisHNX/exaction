import pytest
from calculette import Calculette, Error

@pytest.fixture
def cal():
    return Calculette()


def test_add(cal):
	cal.add(1,2)
	assert cal.res == 3

def test_div(cal):
	cal.divide(1,2)
	assert cal.res == 0.5

def test_raise(cal):
	with pytest.raises(Error):
		cal.divide(1,0)
