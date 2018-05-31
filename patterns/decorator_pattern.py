# 装饰器模式
__doc__ = """装饰器模式（Decorator Pattern）允许向一个现有的对象添加新的功能，同时又不改变其结构。
          这种类型的设计模式属于结构型模式，它是作为现有的类的一个包装。
          这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，提供了额外的功能。
          """

from functools import wraps


# -------------------------------- python 修饰器实现方案 --------------------------------

def log(content):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print(content, end=' ')
            print("loging...")
            return func(*args, **kw)
        return wrapper
    return decorator


# 相当于log('content')(run(time))
@log('Decorator-Pattern')
def run(time):
    print("run at {}".format(time))


# -------------------------------- 类实现 --------------------------------

class Location:
    def __init__(self, city):
        self._city = city

    def show(self):
        return self._city


class Country(Location):
    def __init__(self, location):
        self._location = location

    def show(self):
        print("{} include ".format("China"), end='')
        return self._location.show()


class Continent(Location):
    def __init__(self, location):
        self._location = location

    def show(self):
        print("{} include ".format('Asia'), end='')
        return self._location.show()


if __name__ == '__main__':
    run('2018-05-29')
    # output: Decorator-Pattern loging...
    #         run at 2018-05-29

    location = Location('ShangHai')
    location_detail = Continent(Country(location))
    print(location.show())
    # output: ShangHai
    print(location_detail.show())
    # output: Asia include China include ShangHai
