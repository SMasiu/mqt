from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION


def divide_int_by_int(number1, number2):
    pass


def divide_fraction_by_int(number1, number2):
    pass


def divide_fraction_by_fraction(number1, number2):
    pass


def divide_decimal_fraction_by_int(number1, number2):
    pass


def divide_decimal_fraction_by_fraction(number1, number2):
    pass


def divide_decimal_fraction_by_decimal_fraction(number1, number2):
    pass


division_matching = OperationMatching([
    Operation(MQT_INT, MQT_INT, divide_int_by_int),
    Operation(MQT_FRACTION, MQT_INT, divide_fraction_by_int),
    Operation(MQT_FRACTION, MQT_FRACTION, divide_fraction_by_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_INT, divide_decimal_fraction_by_int),
    Operation(MQT_DECIMAL_FRACTION, MQT_FRACTION, divide_decimal_fraction_by_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_DECIMAL_FRACTION, divide_decimal_fraction_by_decimal_fraction)
])
