from abc import ABC, abstractmethod


class MqtNumber(ABC):
    __type = None

    @property
    def type(self):
        return self.__type

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

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
