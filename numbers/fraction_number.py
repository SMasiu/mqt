import json
from numbers.int_number import MqtInt
from numbers.number_types import MQT_FRACTION
from numbers.mqt_number import MqtNumber


class MqtFraction(MqtNumber):
    __type = MQT_FRACTION

    @property
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

    def value_to_str(self) -> str:
        return json.dumps({'numerator': self.numerator, 'denominator': self.denominator})
