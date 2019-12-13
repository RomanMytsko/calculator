import unittest
from calculator import Calculator, check_input_num
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


def test_regex():
    assert calculator.parse_expression('1+2') == (1, 2, '+')
    assert calculator.parse_expression('4/7') == (4, 7, '/')
    assert calculator.parse_expression('123.3-0') == (123.3, 0, '-')
    assert calculator.parse_expression('0.1*5') == (0.1, 5, '*')
    assert calculator.parse_expression('0jhg') == False


@patch('db_connector_alchemy.AlchemyActions.output_user_actions_count')
def test_output_user_actions_count(print_string):
    print_string.return_value = ' you did 39 actions before!'
    alchemy_actions = session.AlchemyActions()
    r = alchemy_actions.output_user_actions_count('roman')
    assert r == ' you did 39 actions before!'


@patch('calculator.user_input')
def test_user_input(some_text):
    calculator.user_input.return_value = 'roman'
    our_user = calculator.user_input()
    assert our_user == 'roman'


if __name__ == '__main__':
    unittest.main()
