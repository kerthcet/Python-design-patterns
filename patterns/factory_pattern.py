# 简单工厂模式
__doc__ = """工厂模式（Factory Pattern）是 Java 中最常用的设计模式之一。
          这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
          在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。
          """

from abc import ABC, abstractmethod


class DogFactory:
    def get_pet(self):
        return Dog


class CatFactory:
    def get_pet(self):
        return Cat


class PetFactory:
    MAP = {
        'cat': CatFactory,
        'dog': DogFactory
    }

    @classmethod
    def get_factory(cls, name):
        if name in cls.MAP:
            return cls.MAP[name]
        raise TypeError('Unknown pet.')


# 定义为抽象基类的子类，只是为了使用abstractmethod
# 表明所用的模式
class Pet(ABC):
    @abstractmethod
    def roar(self):
        pass


class Dog(Pet):
    def roar(self):
        print("汪汪汪。。。")


class Cat(Pet):
    def roar(self):
        print("喵喵喵。。。")


if __name__ == '__main__':
    factory = PetFactory.get_factory('dog')
    pet = factory().get_pet()
    pet().roar()

    # output
    # 汪汪汪
