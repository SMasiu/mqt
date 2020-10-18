class Operation:
    def __init__(self, _type1, _type2, _function):
        self.type1 = _type1
        self.type2 = _type2
        self.function = _function

    def mach(self, type1, type2) -> bool:
        return (self.type1 == type1 and self.type2 == type2) or (self.type2 == type1 and self.type1 == type2)


class OperationMatching:
    def __init__(self, _operations):
        self.operations = _operations

    def use_operation(self, type1, type2):
        for operation in self.operations:
            if operation.mach(type1, type2):
                return operation.function
