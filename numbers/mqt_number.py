from abc import ABC, abstractmethod
from math_operations.addition import addition_matching
from math_operations.subtraction import subtraction_matching


class MqtNumber(ABC):
    __type: str
    __is_negative: bool

    @property
    def type(self):
        return self.__type

    @property
    def is_negative(self) -> bool:
        return self.__is_negative

    @abstractmethod
    def value_to_str(self) -> str:
        pass

    # --- arithmetic operations ---

    def add(self, other):
        return addition_matching.use_operation(self.type, other.type)(self, other)

    def subtract(self, other):
        return subtraction_matching.use_operation(self.type, other.type)(self, other)

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass

    # operation +
    def __add__(self, other):
        return self.add(other)

    # operation -
    def __sub__(self, other):
        return self.subtract(other)

    # operation *
    def __mul__(self, other):
        return self.multiply(other)

    # operation /
    def __truediv__(self, other):
        return self.divide(other)

    # operation =
    def __eq__(self, other):
        pass

    # operation !=
    def __ne__(self, other):
        pass

    # operation <
    def __lt__(self, other):
        pass

    # operation <=
    def __le__(self, other):
        pass

    # operation >
    def __gt__(self, other):
        pass

    # operation >=
    def __ge__(self, other):
        pass
