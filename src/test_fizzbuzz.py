from fizzbuzz import fizz_buzz

def test_3():
    assert fizz_buzz(3) == "fizz"

def test_5():
    assert fizz_buzz(5) == "buzz"

def test_15():
    assert fizz_buzz(15) == "fizzbuzz"

def test_30():
    assert fizz_buzz(30) == "fizzbuzz"