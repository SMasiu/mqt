from common.operation_matching import Operation, OperationMatching
from numbers.number_types import MQT_INT, MQT_FRACTION, MQT_DECIMAL_FRACTION
from transformations.bring_down_to_common_denominator import bring_down_to_common_denominator
from transformations.reduce_fraction import reduce_fraction


def add_int_to_int(number1, number2):
    from numbers.int_number import MqtInt
    return MqtInt(number1.value + number2.value)


def add_fraction_to_int(number1, number2):
    pass


def add_fraction_to_fraction(number1, number2):
    from numbers.fraction_number import MqtFraction
    from numbers.int_number import MqtInt
    if number1.denominator == number2.denominator:
        return reduce_fraction(MqtFraction({
            'numerator': MqtInt((number1.numerator + number2.numerator).value),
            'denominator': MqtInt(number1.denominator.value)
        }))

    num1, num2 = bring_down_to_common_denominator(number1, number2)

    return reduce_fraction(MqtFraction({
        'numerator': MqtInt((num1.numerator + num2.numerator).value),
        'denominator': MqtInt(num1.denominator.value)
    }))


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
