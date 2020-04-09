#
#Python内置的@property装饰器就是负责把一个方法变成属性调用
#
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# >>> s = Student()
# >>> s.set_score(60) # ok!
# >>> s.get_score()
# 60
# >>> s.set_score(9999)
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!




class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# >>> s.score = 9999 #既能检查参数，又可以用属性这样简单的方式来访问类的变量
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!