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

# 装饰类
class Skill:
    def __init__(self, name):
        self._name = name

    def learn_skill(self):
        print("learn skill: {}".format(self._name))


class SkillQ(Skill):
    def __init__(self, skill):
        self._skill = skill

    def learn_skill(self):
        print("learning Q skill...")
        return self._skill.learn_skill()


class SkillW(Skill):
    def __init__(self, skill):
        self._skill = skill

    def learn_skill(self):
        print("learning W skill...")
        return self._skill.learn_skill()

if __name__ == '__main__':
    run('2018-05-29')
    # output: Decorator-Pattern loging...
    #         run at 2018-05-29

    skill = Skill('Learn two skills...')
    skill.learn_skill() # output: learn skill: Learn two skills...

    q = SkillQ(skill)
    w = SkillW(q)
    w.learn_skill()
    # output: learning W skill...
    #         learning Q skill...
    #         learn skill: Learn two skills...
