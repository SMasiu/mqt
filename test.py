from numbers.int_number import MqtInt
from numbers.fraction_number import MqtFraction
from numbers.decimal_fraction_number import MqtDecimalFraction


def should(result, correct_value):
    return result.value == correct_value.value


def calculate_result(operations):
    num1, sign, num2 = operations
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2


def test():
    # --- testing data ---
    num_int1 = MqtInt(20)
    num_int2 = MqtInt(0)
    num_int3 = MqtInt(-25)
    num_int4 = MqtInt(122)

    num_fraction1 = MqtFraction(MqtInt(2), MqtInt(5))
    num_fraction2 = MqtFraction(MqtInt(-5), MqtInt(9))
    num_fraction3 = MqtFraction(MqtInt(2), MqtInt(-5))

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
    ]

    # --- test output ---

    passed = 0
    failed = []

    for operations, correct_answer in tests:
        result = calculate_result(operations)
        if not should(result, correct_answer):
            failed.append([operations, correct_answer])
            print("\033[91mTest failed on input {} {} {}. Given output {} Expected output {}".format(
                operations[0].value,
                operations[1],
                operations[2].value,
                result.value,
                correct_answer.value
            ))
        else:
            print("\033[92mTest passed on input {} {} {}. Given output {}".format(
                operations[0].value,
                operations[1],
                operations[2].value,
                result.value
            ))
            passed += 1

    print("\033[94mPassed {} out of {}".format(passed, len(tests)))


test()
