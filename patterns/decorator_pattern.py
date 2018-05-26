# 装饰器模式
__doc__ = """装饰器模式（Decorator Pattern）允许向一个现有的对象添加新的功能，同时又不改变其结构。
          这种类型的设计模式属于结构型模式，它是作为现有的类的一个包装。
          这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，提供了额外的功能。
          """


class Hero:
    def learn_skill(self):
        print("学习技能")


# 装饰类
class AddSkill(Hero):
    def pick_hero(self, hero):
        self._hero = hero

    def learn_skill(self):
        print("学习完技能")
        self._hero.learn_skill()


class SkillQ(AddSkill):
    def learn_skill(self):
        print("学习Q技能")
        self._hero.learn_skill()


class SkillW(AddSkill):
    def learn_skill(self):
        print("学习W技能")
        self._hero.learn_skill()


if __name__ == '__main__':
    hero = Hero()

    q = SkillQ()
    q.pick_hero(hero)
    w = SkillW()
    w.pick_hero(q)  # 层层递进传参

    w.learn_skill()
