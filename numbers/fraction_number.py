import json
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

    def __init__(self, fraction):
        self.__numerator = fraction['numerator']
        self.__denominator = fraction['denominator']

    def value_to_str(self) -> str:
        return json.dumps({'numerator': self.numerator.value, 'denominator': self.denominator.value})
