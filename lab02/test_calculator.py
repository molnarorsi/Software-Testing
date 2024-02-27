import calculator

def test_addition():
    output = calculator.add(1, 2)
    assert output == 3

def test_subtraction():
    output = calculator.subtract(3, 1)
    assert output == 2

def test_multiplication():
    output = calculator.multiply(2, 3)
    assert output == 6