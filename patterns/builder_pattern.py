# 建造者模式
__doc__ = """建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。
             这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
             一个 Builder 类会一步一步构造最终的对象。该Builder类是独立于其他对象的。
             通过一个创建者按照对象的创建步骤来一步步执行对象的创建，
             当需要创建不同的对象时，只需要派生一个具体的建造者，重写相应的组件构建方法即可
          """


class Kfc:
    def __init__(self):
        self.get_drink()
        self.get_food()

    def get_drink(self):
        raise NotImplementedError

    def get_food(self):
        raise NotImplementedError

    def __repr__(self):
        return 'You ordered {} and {}.'.format(self.food, self.drink)


class ChickenMeal(Kfc):
    def get_drink(self):
        self.drink = 'coca cola'

    def get_food(self):
        self.food = 'chicken leg'


class HambergerMeal(Kfc):
    def get_drink(self):
        self.drink = 'milk tea'

    def get_food(self):
        self.food = 'double hamburger'


class Order:
    def have_my_order(self, meal):
        print(meal)


if __name__ == '__main__':
    order = Order()
    chicken_meal = ChickenMeal()
    hamburger_meal = HambergerMeal()

    order.have_my_order(chicken_meal)
    # output: You ordered chicken leg and coca cola.

    order.have_my_order(hamburger_meal)
    # output: You ordered double hamburger and milk tea.
