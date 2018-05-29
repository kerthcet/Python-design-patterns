# 装饰器模式
__doc__ = """装饰器模式（Decorator Pattern）允许向一个现有的对象添加新的功能，同时又不改变其结构。
          这种类型的设计模式属于结构型模式，它是作为现有的类的一个包装。
          这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，提供了额外的功能。
          """

from functools import wraps


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


if __name__ == '__main__':
    run('2018-05-29')
