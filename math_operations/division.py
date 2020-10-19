from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION
from operations.greatest_common_divisor import greatest_common_divisor


def divide_int_by_int(number1, number2):
    from numbers.int_number import MqtInt

    if number1 == number2:
        return MqtInt(1)

    if number1.value == 0:
        return MqtInt(0)

    divisor = greatest_common_divisor(number1.value, number2.value)

    if divisor == number2.value:
        return MqtInt(int(number1.value / divisor))

    from numbers.fraction_number import MqtFraction
    return MqtFraction({
        'numerator': MqtInt(int(number1.value / divisor)),
        'denominator': MqtInt(int(number2.value / divisor))
    })


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
