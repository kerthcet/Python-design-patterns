# 单例模式
from functools import wraps

__doc__ = """单例模式（Singleton ）是 Java 中最简单的设计模式之一。
          这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
          这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。
          这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。
          """


# 类方法实现单例
class Singleton1:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance


# 修饰器实现单例
def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance


@singleton
class Singleton2:
    pass


# 元类实现
class Singleton3(type):
    _instances = {}

    def __call__(cls, *args, **kw):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kw)
        return cls._instances[cls]


class TestSingleton(metaclass=Singleton3):
    pass


if __name__ == '__main__':
    x1 = Singleton1()
    y1 = Singleton1()
    assert id(x1) == id(y1)

    x2 = Singleton2()
    y2 = Singleton2()
    assert id(x2) == id(y2)

    x3 = TestSingleton()
    y3 = TestSingleton()
    assert id(x3) == id(y3)
