from numbers.mqt_number import MqtNumber
from numbers.number_types import MQT_DECIMAL_FRACTION


class MqtDecimalFraction(MqtNumber):
    __type = MQT_DECIMAL_FRACTION

    @property
    def type(self):
        return self.__type

    @property
    def value(self):
        return self.__value

    def __init__(self, value: float):
        self.__value = value

    def value_to_str(self) -> str:
        return str(self.value)
