
# Uzycie biblioteki pytest
import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(10, 10) == 20


def test_div():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.div(5,0)

testdata = [(1,2,3), (2,3,5), (8,-6,2) ]
@pytest.mark.parametrize("a, b, result", testdata)
def test_add2(a, b, result):
    calc = Calculator()
    assert calc.add(a,b) == result

@pytest.fixture
def numbers_data():
    return [
        {"value" : 30},
        {"value" : 20}
    ]

def test_numbers_positive(numbers_data):
    assert all([ n["value"]>0 for n in numbers_data])