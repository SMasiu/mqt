from numbers.int_number import MqtInt
from numbers.fraction_number import MqtFraction
from numbers.decimal_fraction_number import MqtDecimalFraction


def should(result, correct_value):
    return result == correct_value


def calculate_result(operations):
    num1, sign, num2 = operations
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2


def test():
    # --- testing data ---
    num_int1 = MqtInt(20)
    num_int2 = MqtInt(0)
    num_int3 = MqtInt(-25)
    num_int4 = MqtInt(122)
    num_int5 = MqtInt(4)
    num_int6 = MqtInt(9)
    num_int7 = MqtInt(3)

    num_fraction1 = MqtFraction({'numerator': MqtInt(2), 'denominator': MqtInt(5)})
    num_fraction2 = MqtFraction({'numerator': MqtInt(3), 'denominator': MqtInt(4)})
    num_fraction3 = MqtFraction({'numerator': MqtInt(-5), 'denominator':  MqtInt(9)})
    num_fraction4 = MqtFraction({'numerator': MqtInt(2), 'denominator': MqtInt(-5)})
    num_fraction5 = MqtFraction({'numerator': MqtInt(1), 'denominator': MqtInt(3)})
    num_fraction6 = MqtFraction({'numerator': MqtInt(2), 'denominator': MqtInt(3)})
    num_fraction7 = MqtFraction({'numerator': MqtInt(4), 'denominator': MqtInt(3)})
    num_fraction8 = MqtFraction({'numerator': MqtInt(1), 'denominator': MqtInt(9)})
    num_fraction9 = MqtFraction({'numerator': MqtInt(0), 'denominator': MqtInt(3)})
    num_fraction10 = MqtFraction({'numerator': MqtInt(-2), 'denominator': MqtInt(-3)})

    num_decimal_fraction1 = MqtDecimalFraction(0.235)
    num_decimal_fraction2 = MqtDecimalFraction(-0.12)
    num_decimal_fraction3 = MqtDecimalFraction(0.0025)

    # --- testing operations ---

    tests = [
        [(num_int1, '+', num_int4), MqtInt(142)],
        [(num_int1, '+', num_int2), MqtInt(20)],
        [(num_int3, '+', num_int1), MqtInt(-5)],

        [(num_int1, '-', num_int4), MqtInt(-102)],
        [(num_int4, '-', num_int1), MqtInt(102)],
        [(num_int3, '-', num_int1), MqtInt(-45)],
        [(num_int1, '-', num_int3), MqtInt(45)],
        [(num_int1, '-', num_int2), MqtInt(20)],
        [(num_int2, '-', num_int1), MqtInt(-20)],

        [(num_int1, '*', num_int5), MqtInt(80)],
        [(num_int5, '*', num_int1), MqtInt(80)],
        [(num_int3, '*', num_int5), MqtInt(-100)],
        [(num_int5, '*', num_int3), MqtInt(-100)],
        [(num_int4, '*', num_int2), MqtInt(0)],
        [(num_int2, '*', num_int4), MqtInt(0)],
        [(num_int3, '*', num_int2), MqtInt(0)],
        [(num_int2, '*', num_int3), MqtInt(0)],

        [(num_int6, '/', num_int7), MqtInt(3)],
        [(num_int7, '/', num_int6), MqtFraction({'numerator': MqtInt(1), 'denominator': MqtInt(3)})],
        [(num_int6, '/', num_int6), MqtInt(1)],
        [(num_int5, '/', num_int1), MqtFraction({'numerator': MqtInt(1), 'denominator': MqtInt(5)})],
        [(num_int1, '/', num_int5), MqtInt(5)],
        [(num_int2, '/', num_int6), MqtInt(0)],
        [(num_int4, '/', num_int6), MqtFraction({'numerator': MqtInt(122), 'denominator': MqtInt(9)})],

        [(num_fraction1, '+', num_fraction2), MqtFraction({'numerator': MqtInt(23), 'denominator': MqtInt(20)})],
        [(num_fraction2, '+', num_fraction2), MqtFraction({'numerator': MqtInt(3), 'denominator': MqtInt(2)})],
        [(num_fraction3, '+', num_fraction3), MqtFraction({'numerator': MqtInt(-10), 'denominator': MqtInt(9)})],
        [(num_fraction3, '+', num_fraction5), MqtFraction({'numerator': MqtInt(-2), 'denominator': MqtInt(9)})],
        [(num_fraction4, '+', num_fraction5), MqtFraction({'numerator': MqtInt(-1), 'denominator': MqtInt(15)})],
        [(num_fraction3, '+', num_fraction4), MqtFraction({'numerator': MqtInt(-43), 'denominator': MqtInt(45)})],
        [(num_fraction5, '+', num_fraction6), MqtInt(1)],

        [(num_fraction1, '-', num_fraction2), MqtFraction({'numerator': MqtInt(-7), 'denominator': MqtInt(20)})],
        [(num_fraction2, '-', num_fraction2), MqtInt(0)],
        [(num_fraction3, '-', num_fraction3), MqtInt(0)],
        [(num_fraction3, '-', num_fraction6), MqtFraction({'numerator': MqtInt(-11), 'denominator': MqtInt(9)})],
        [(num_fraction6, '-', num_fraction3), MqtFraction({'numerator': MqtInt(11), 'denominator': MqtInt(9)})],
        [(num_fraction7, '-', num_fraction5), MqtInt(1)],
        [(num_fraction3, '-', num_fraction8), MqtFraction({'numerator': MqtInt(-2), 'denominator': MqtInt(3)})],

        [(num_fraction1, '*', num_fraction2), MqtFraction({'numerator': MqtInt(3), 'denominator': MqtInt(10)})],
        [(num_fraction2, '*', num_fraction3), MqtFraction({'numerator': MqtInt(-5), 'denominator': MqtInt(12)})],
        [(num_fraction4, '*', num_fraction6), MqtFraction({'numerator': MqtInt(-4), 'denominator': MqtInt(15)})],
        [(num_fraction3, '*', num_fraction4), MqtFraction({'numerator': MqtInt(2), 'denominator': MqtInt(9)})],
        [(num_fraction1, '*', num_fraction9), MqtInt(0)],
        [(num_fraction6, '*', num_fraction10), MqtFraction({'numerator': MqtInt(4), 'denominator': MqtInt(9)})],
        [(num_fraction10, '*', num_fraction10), MqtFraction({'numerator': MqtInt(4), 'denominator': MqtInt(9)})],

        [(num_fraction1, '/', num_fraction2), MqtFraction({'numerator': MqtInt(8), 'denominator': MqtInt(15)})],
        [(num_fraction2, '/', num_fraction3), MqtFraction({'numerator': MqtInt(-27), 'denominator': MqtInt(20)})],
        [(num_fraction4, '/', num_fraction6), MqtFraction({'numerator': MqtInt(-3), 'denominator': MqtInt(5)})],
        [(num_fraction3, '/', num_fraction4), MqtFraction({'numerator': MqtInt(25), 'denominator': MqtInt(18)})],
        [(num_fraction6, '/', num_fraction10), MqtInt(1)],
        [(num_fraction10, '/', num_fraction10), MqtInt(1)],
    ]

    # --- test output ---

    passed = 0
    failed = []

    for operations, correct_answer in tests:
        result = calculate_result(operations)
        if not should(result, correct_answer):
            failed.append([operations, correct_answer])
            print("\033[91mTest failed on input {} {} {}. Given output {} Expected output {}".format(
                operations[0].value_to_str(),
                operations[1],
                operations[2].value_to_str(),
                result.value_to_str(),
                correct_answer.value_to_str()
            ))
        else:
            print("\033[92mTest passed on input {} {} {}. Given output {}".format(
                operations[0].value_to_str(),
                operations[1],
                operations[2].value_to_str(),
                result.value_to_str()
            ))
            passed += 1

    print("\033[94mPassed {} out of {}".format(passed, len(tests)))


test()
