import pytest
def square(n):
    return n**2

def cube(n):
    return n**3

def fifith_power(n):
    return n**5

def test_square():
    assert square(2)==4,'test failed square of 2 should be 4'
    assert square(3)==9,'test fialed sqaure of 3 should be 9'

def test_cube():
    assert cube(2)==8,'test failed cube of 2 should be 9'
    assert cube(3)==27,'test fialed cube of 3 should be 27'

def test_square():
    assert fifith_power(2)==32,'test failed fifith_power of 2 should be 32'
    assert fifith_power(3)==243,'test fialed fifith_power of 3 should be 243'

def text_input_test():
    with pytest.raises(TypeError):
        square('string')
