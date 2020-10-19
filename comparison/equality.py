from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION


def is_equal_int_to_int(number1, number2):
    return number1.value == number2.value


def is_equal_fraction_to_int(number1, number2):
    pass


def is_equal_fraction_to_fraction(number1, number2):
    return number1.numerator.value == number2.numerator.value and number1.denominator.value == number2.denominator.value


def is_equal_decimal_fraction_to_int(number1, number2):
    pass


def is_equal_decimal_fraction_to_fraction(number1, number2):
    pass


def is_equal_decimal_fraction_to_decimal_fraction(number1, number2):
    pass


equality_matching = OperationMatching([
    Operation(MQT_INT, MQT_INT, is_equal_int_to_int),
    Operation(MQT_FRACTION, MQT_INT, is_equal_fraction_to_int),
    Operation(MQT_FRACTION, MQT_FRACTION, is_equal_fraction_to_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_INT, is_equal_decimal_fraction_to_int),
    Operation(MQT_DECIMAL_FRACTION, MQT_FRACTION, is_equal_decimal_fraction_to_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_DECIMAL_FRACTION, is_equal_decimal_fraction_to_decimal_fraction)
])
