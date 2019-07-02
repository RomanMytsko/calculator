from calculator import Calculator, check_input_num
# from calculator import check_input_num


def test_addition():
    calc = Calculator (1, 2, '+')
    res = calc.calculate ()
    assert res == 3


def test_subtraction():
    calc = Calculator (5, 3, "-")
    res = calc.calculate ()
    assert res == 2


def test_multiplication():
    calc = Calculator (2, 8, "*")
    assert calc.calculate () == 16


def test_division():
    calc = Calculator (12, 2, "/")
    assert calc.calculate () == 6


def test_check_input_num():
    number = "4"
    assert check_input_num (number) == 4
    number = "r"
    assert check_input_num (number) == False


def test_calculate():
    r = Calculator (3, 3, "+")
    assert r.calculate () == r.addition ()
    r = Calculator (3, 4, "-")
    assert r.calculate () == r.subtraction ()
    r = Calculator (3, 4, "*")
    assert r.calculate () == r.multiplication ()
    r = Calculator (3, 4, "/")
    assert r.calculate () == r.division ()
