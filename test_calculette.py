import pytest
from calculette import Calculette, Error

@pytest.fixture
def cal():
    return Calculette()


def test_add(cal):
	cal.add(1,10)
	assert cal.res == 9

def test_div(cal):
	cal.divide(1,9)
	assert cal.res == 0.13

def test_raise(cal):
	with pytest.raises(Error):
		cal.divide(1,0)
