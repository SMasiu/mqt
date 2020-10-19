from operations.least_common_multiple import least_common_multiple


def bring_down_to_common_denominator(fraction1, fraction2):
    numerator1 = fraction1.numerator.value
    denominator1 = fraction1.denominator.value

    numerator2 = fraction2.numerator.value
    denominator2 = fraction2.denominator.value

    if denominator1 == denominator2:
        return fraction1, fraction2

    lcm = least_common_multiple(denominator1, denominator2)

    m1 = int(lcm / denominator1)
    m2 = int(lcm / denominator2)

    from numbers.fraction_number import MqtFraction
    from numbers.int_number import MqtInt
    return MqtFraction({
        'numerator': MqtInt(numerator1 * m1),
        'denominator': MqtInt(denominator1 * m1)
    }), MqtFraction({
        'numerator': MqtInt(numerator2 * m2),
        'denominator': MqtInt(denominator2 * m2)
    })
