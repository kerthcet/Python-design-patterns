# 简单工厂模式
__doc__ = """工厂模式（Factory Pattern）是 Java 中最常用的设计模式之一。
          这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
          在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。
          """


class Operation:
    def __init__(self, number1, number2):
        self._number1 = number1
        self._number2 = number2

    def get_result(self):
        pass


class Add(Operation):
    def __init__(self, number1, number2):
        super().__init__(number1=number1, number2=number2)

    def get_result(self):
        return self._number1 + self._number2


class Sub(Operation):
    def __init__(self, number1, number2):
        super().__init__(number1=number1, number2=number2)

    def get_result(self):
        return abs(self._number1 - self._number2)


class OperationFactory:
    MAP = {
        'add': Add,
        'sub': Sub
    }

    def __init__(self, operation):
        self._operation = operation

    def get_operation(self):
        return self.MAP[self._operation]


if __name__ == '__main__':
    factory = OperationFactory(operation='add')
    operation = factory.get_operation()
    x, y = 10, 80
    print(operation(number1=x, number2=y).get_result())
