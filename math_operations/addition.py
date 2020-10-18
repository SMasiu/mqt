from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION


def add_int_to_int(number1, number2):
    from numbers.int_number import MqtInt
    return MqtInt(number1.value + number2.value)


def add_fraction_to_int(number1, number2):
    pass


def add_fraction_to_fraction(number1, number2):
    pass


def add_decimal_fraction_to_int(number1, number2):
    pass


def add_decimal_fraction_to_fraction(number1, number2):
    pass


def add_decimal_fraction_to_decimal_fraction(number1, number2):
    pass


addition_matching = OperationMatching([
    Operation(MQT_INT, MQT_INT, add_int_to_int),
    Operation(MQT_FRACTION, MQT_INT, add_fraction_to_int),
    Operation(MQT_FRACTION, MQT_FRACTION, add_fraction_to_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_INT, add_decimal_fraction_to_int),
    Operation(MQT_DECIMAL_FRACTION, MQT_FRACTION, add_decimal_fraction_to_fraction),
    Operation(MQT_DECIMAL_FRACTION, MQT_DECIMAL_FRACTION, add_decimal_fraction_to_decimal_fraction)
])
