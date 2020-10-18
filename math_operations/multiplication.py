from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION


def multiply_int_by_int(number1, number2):
    pass


def multiply_fraction_by_int(number1, number2):
    pass


def multiply_fraction_by_fraction(number1, number2):
    pass


def multiply_decimal_fraction_by_int(number1, number2):
    pass


def multiply_decimal_fraction_by_fraction(number1, number2):
    pass


def multiply_decimal_fraction_by_decimal_fraction(number1, number2):
    pass


multiplication_matching = OperationMatching([
    Operation(MQT_INT, MQT_INT, multiply_int_by_int),
    Operation(MQT_FRACTION, MQT_INT, multiply_fraction_by_int),
    Operation(MQT_FRACTION, MQT_FRACTION, multiply_fraction_by_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_INT, multiply_decimal_fraction_by_int),
    Operation(MQT_DECIMAL_FRACTION, MQT_FRACTION, multiply_decimal_fraction_by_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_DECIMAL_FRACTION, multiply_decimal_fraction_by_decimal_fraction)
])
