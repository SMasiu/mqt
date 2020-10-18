from numbers.mqt_number import MqtNumber
from numbers.number_types import MQT_DECIMAL_FRACTION


class MqtDecimalFraction(MqtNumber):
    __type = MQT_DECIMAL_FRACTION

    def type(self):
        return self.__type

    @property
    def value(self):
        return self.__value

    def __init__(self, value: float):
        self.__value = value

    def add(self, other):
        pass

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass

    def divide(self, other):
        pass
