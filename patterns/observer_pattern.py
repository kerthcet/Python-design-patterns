# 观察者模式
__doc__ = """观察者模式(Observer Pattern)：定义对象间的一种一对多依赖关系，
             使得每当一个对象状态发生改变时，其相关依赖对象皆得到通知并被自动更新。
             观察者模式又叫做发布-订阅（Publish/Subscribe）模式、
             模型-视图（Model/View）模式、源-监听器（Source/Listener）模式
             或从属者（Dependents）模式。
             观察者模式是一种对象行为型模式。
          """

import datetime


# 订阅主题
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def push(self):
        print("开始订阅。。。")
        for observer in self._observers:
            observer.notify()


class Data(Subject):
    def __init__(self, title='blank'):
        super().__init__()
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.push()


class Observer1:
    def notify(self):
        print(str(datetime.datetime.now()), end=', ')
        print("{} updating...".format('Observer1'))


class Observer2:
    def notify(self):
        print(str(datetime.datetime.now()), end=', ')
        print("{} updating...".format('Observer2'))


if __name__ == '__main__':
    observer1 = Observer1()
    observer2 = Observer2()
    data = Data()

    data.subscribe(observer1)
    data.subscribe(observer2)

    data.title = '开始订阅'
    # output: 开始订阅。。。
    #         2018-05-31 01:56:07.312823, Observer1 updating...
    #         2018-05-31 01:56:07.312847, Observer2 updating...

    data.unsubscribe(observer1)
    data.title = 'observer1取消订阅'
    # output: 开始订阅。。。
    #         2018-05-31 01:56:07.312860, Observer2 updating...
