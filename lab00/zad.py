# Zad.1
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

@property
def x(self):
    return self._x

@property
def y(self):
    return self._y

@x.setter
def x(self, value):
    self._x = value

@y.setter
def y(self, value):
    self._y = value

point1 = Point()
point1.x = 2
point1.y = 5
print(point1.x, point1.y)

# Zad.2
def Validator(min_val, max_val):
    def decorator(fun):
        def wrapper(point1, point2):
            coordinates = (point1.x, point1.y, point2.x, point2.y)
            for coordinate in coordinates:
                if coordinate < min_val or coordinate > max_val:
                    raise ValueError
            return fun(point1, point2)
        return wrapper
    return decorator

@Validator(1, 5)
def addPoints(point1, point2):
    result = Point()
    result.x = point1.x + point2.x
    result.y = point1.y + point2.y
    return result.x, result.y

@Validator(1, 5)
def substractPoints(point1, point2):
    result = Point()
    result.x = point1.x - point2.x
    result.y = point1.y - point2.y
    return result.x, result.y

point1 = Point()
point1.x = 3
point1.y = 2

point2 = Point()
point2.x = 1
point2.y = 1

point3 = Point()
point3.x = 7
point3.y = -6

print(addPoints(point1, point2))
print(substractPoints(point1, point2))
# print(addPoints(point1, point3))
# print(substractPoints(point1, point3))

# Zad.3
import math

class Calculate:
    @staticmethod
    def obwodTrojkata(point1, point2, point3):
        return Calculate.calculateSide(point1, point2) + Calculate.calculateSide(point2, point3) + Calculate.calculateSide(point1, point3)
    
    @staticmethod
    def obwodCzworokata(point1, point2, point3, point4):
        return Calculate.calculateSide(point1, point2) + Calculate.calculateSide(point1, point4) + Calculate.calculateSide(point2, point3) + Calculate.calculateSide(point3, point4)

    @staticmethod
    def Heron(point1, point2, point3):
        L = Calculate.obwodTrojkata(point1, point2, point3)
        p = L/2
        return (p*(p-Calculate.calculateSide(point1, point2))*(p-Calculate.calculateSide(point2, point3))*(p-Calculate.calculateSide(point1, point3)))**(1/2)

    @staticmethod
    def Brahmagupta(point1, point2, point3, point4):
        L = Calculate.obwodCzworokata(point1, point2, point3, point4)
        p = L/2
        return ((p-Calculate.calculateSide(point1, point2))*(p-Calculate.calculateSide(point1, point4))*(p-Calculate.calculateSide(point2, point3))*(p-Calculate.calculateSide(point3, point4)))**(1/2)
    
    @staticmethod
    def calculateSide(point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

point1 = Point()
point1.x = 0
point1.y = 4

point2 = Point()
point2.x = 0
point2.y = 0

point3 = Point()
point3.x = 4
point3.y = 0

point4 = Point()
point4.x = 4
point4.y = 4

print(Calculate.obwodTrojkata(point1, point2, point3))
print(Calculate.obwodCzworokata(point1, point2, point3, point4))
print(Calculate.Heron(point1, point2, point3))
print(Calculate.Brahmagupta(point1, point2, point3, point4))

# Zad.4
class CallsCounter:
    count = {}

    def __init__(self, fun):
        self._fun = fun
        CallsCounter.count[self] = 0

    def __call__(self, *p):
        CallsCounter.count[self] += 1
        return self._fun(*p)

    @staticmethod
    def getCount(fun):
        return CallsCounter.count[fun]

@CallsCounter
def test():
    return 0

@CallsCounter
def test2(a, *b):
    return 0

test()
print(CallsCounter.getCount(test))

test()
print(CallsCounter.getCount(test))

test2(1, [2,])
print(CallsCounter.getCount(test2))

test2(1, [2,])
print(CallsCounter.getCount(test2))

f = test2
f(1, [2,])
print(CallsCounter.getCount(test2))
print(CallsCounter.getCount(f))