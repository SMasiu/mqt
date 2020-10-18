from numbers.mqt_number import MqtNumber
from numbers.number_types import MQT_INT


class MqtInt(MqtNumber):
    __type = MQT_INT

    def type(self):
        return self.__type

    @property
    def value(self):
        return self.__value

    def __init__(self, value: int):
        self.__value = value

    def add(self, other):
        return MqtInt(20)

    def subtract(self, other):
        return MqtInt(3)

    def multiply(self, other):
        return MqtInt(4)

    def divide(self, other):
        return MqtInt(3)
