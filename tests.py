from calculator import Calculator, check_input_num
import db_connector_alchemy
from unittest.mock import patch
import calculator
import db_connector_alchemy as session


def test_addition():
    calc = Calculator(1, 2, '+')
    res = calc.calculate()
    assert res == 3


def test_subtraction():
    calc = Calculator(5, 3, "-")
    res = calc.calculate()
    assert res == 2


def test_multiplication():
    calc = Calculator(2, 8, "*")
    assert calc.calculate() == 16


def test_division():
    calc = Calculator(12, 2, "/")
    assert calc.calculate() == 6


def test_check_input_num():
    number = "4"
    assert check_input_num(number) == 4
    number = "r"
    assert check_input_num(number) == False


def test_calculate():
    r = Calculator(3, 3, "+")
    assert r.calculate() == r.addition()
    r = Calculator(3, 4, "-")
    assert r.calculate() == r.subtraction()
    r = Calculator(3, 4, "*")
    assert r.calculate() == r.multiplication()
    r = Calculator(3, 4, "/")
    assert r.calculate() == r.division()


# @patch('db_connector_alchemy.SQLAlchemyDBConnection')
# def test_connection(db):
#     conn = db_connector_alchemy.AlchemyActions()
#     assert 1 == 1


def test_regex():
    assert calculator.our_data('1+2') == (1, 2, '+')
    assert calculator.our_data('4/7') == (4, 7, '/')
    assert calculator.our_data('123.3-0') == (123.3, 0, '-')
    assert calculator.our_data('0.1*5') == (0.1, 5, '*')
    assert calculator.our_data('0jhg') == (False)




#
# @patch('db_connector_alchemy.AlchemyActions.read_user')
# def test_get_id_by_username(read_user):
#     # read_user.return_value = 100500
#     alchemy_actions = session.AlchemyActions()
#     res, a = calculator.get_id_by_username('roman')
#     assert a == 81
#     # assert res == 100500


@patch('db_connector_alchemy.AlchemyActions.utput_user_actions_count')
def output_user_actions_count(print_string):
    print_string.return_value = ' you did 39 actions before!'
    alchemy_actions = session.AlchemyActions()
    r = calculator.printing_sum_of_user_actions(alchemy_actions, 'roman')
    assert r == ' you did 39 actions before!'

@patch('calculator.our_user_string.our_user')
def test_user_input(some_text):
    calculator.our_user.return_value = 'roman'
    our_user = calculator.our_user()
    assert our_user == 'roman'
