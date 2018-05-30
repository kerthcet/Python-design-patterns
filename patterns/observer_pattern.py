# 观察者模式
__doc__ = """观察者模式(Observer Pattern)：定义对象间的一种一对多依赖关系，
             使得每当一个对象状态发生改变时，其相关依赖对象皆得到通知并被自动更新。
             观察者模式又叫做发布-订阅（Publish/Subscribe）模式、
             模型-视图（Model/View）模式、源-监听器（Source/Listener）模式
             或从属者（Dependents）模式。
             观察者模式是一种对象行为型模式。
          """


# 订阅主题
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.push()

    def push(self):
        for observer in self._observers:
            observer.notify()


class Observer:
    def notify(self):
        print("{} updating...".format('Observer'))


class ClientObserver1(Observer):
    def notify(self):
        print("{} updating...".format('Observer'))
