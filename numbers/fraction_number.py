from numbers.int_number import MqtInt
from numbers.number_types import MQT_FRACTION
from numbers.mqt_number import MqtNumber


class MqtFraction(MqtNumber):
    __type = MQT_FRACTION

    def type(self):
        return self.__type

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __init__(self, numerator: MqtInt, denominator: MqtInt):
        self.__numerator = numerator
        self.__denominator = denominator

    def add(self, other):
        pass

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass

    def divide(self, other):
        pass
