from app.demo_pytest import add,div,mul,discount_season
import pytest   #for asserting exception
#to termianl write "pytest"

#Skipping test
@pytest.mark.skip("Skip add test")
def test_add():
    assert add(10,20) == 30

def test_div():
    assert div(100,20) == 5

    #case for asserting exception
    with pytest.raises(ValueError):
        div(4,0)

@pytest.mark.skipif(discount_season() ,reason="skiping cause discount season on")  #içindeki değer True ise skip
def test_mul():
    assert mul(1,20) == 20