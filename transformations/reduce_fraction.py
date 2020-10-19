from operations.greatest_common_divisor import greatest_common_divisor


def reduce_fraction(fraction):
    from numbers.int_number import MqtInt
    numerator = fraction.numerator.value
    denominator = fraction.denominator.value

    if numerator % denominator == 0:
        return MqtInt(int(numerator / denominator))

    gcd = greatest_common_divisor(numerator, denominator)

    if gcd == 1:
        return fraction

    from numbers.fraction_number import MqtFraction

    return MqtFraction({
        'numerator': MqtInt(int(numerator / gcd)),
        'denominator': MqtInt(int(denominator / gcd))
    })
