def reverse_fraction(fraction):
    from numbers.fraction_number import MqtFraction

    return MqtFraction({
        'numerator': fraction.denominator,
        'denominator': fraction.numerator
    })
