from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION


def subtract_int_from_int(number1, number2):
    from numbers.int_number import MqtInt
    return MqtInt(number1.value - number2.value)


def subtract_fraction_from_int(number1, number2):
    pass


def subtract_fraction_from_fraction(number1, number2):
    pass


def subtract_decimal_fraction_from_int(number1, number2):
    pass


def subtract_decimal_fraction_from_fraction(number1, number2):
    pass


def subtract_decimal_fraction_from_decimal_fraction(number1, number2):
    pass


subtraction_matching = OperationMatching([
    Operation(MQT_INT, MQT_INT, subtract_int_from_int),
    Operation(MQT_FRACTION, MQT_INT, subtract_fraction_from_int),
    Operation(MQT_FRACTION, MQT_FRACTION, subtract_fraction_from_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_INT, subtract_decimal_fraction_from_int),
    Operation(MQT_DECIMAL_FRACTION, MQT_FRACTION, subtract_decimal_fraction_from_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_DECIMAL_FRACTION, subtract_decimal_fraction_from_decimal_fraction)
])
