import math

#1
print('Zadanie 1')

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

point1 = Point()
point1.x = 8
point1.y = 4
print('Współrzędne:', point1.x, point1.y)

#2
print('Zadanie 2')

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

@Validator(0, 9)
def addPoints(point1, point2):
    result = Point();
    result.x = point2.x + point1.x
    result.y = point2.y + point1.y
    return result.x, result.y

@Validator(0, 9)
def subtractPoints(point1, point2):
    result = Point();
    result.x = point2.x - point1.x
    result.y = point2.y - point1.y
    return result.x, result.y

point1 = Point(2, 1)
point2 = Point(8, 4)

print(addPoints(point1, point2))
print(subtractPoints(point1, point2))

#3
print('Zadanie 3')

class HeronaBrahmagupty:
    @staticmethod
    def dlugosc(point1, point2):
        return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)
    
    @staticmethod
    def obwodTr(point1, point2, point3):
        return HeronaBrahmagupty.dlugosc(point1, point2) + HeronaBrahmagupty.dlugosc(point2, point3) + HeronaBrahmagupty.dlugosc(point3, point1)
    
    @staticmethod
    def obwodCz(point1, point2, point3, point4):
        return HeronaBrahmagupty.dlugosc(point1, point2) + HeronaBrahmagupty.dlugosc(point2, point3) + HeronaBrahmagupty.dlugosc(point3, point4) + HeronaBrahmagupty.dlugosc(point4, point1)
    
    @staticmethod
    def Heron(point1, point2, point3):
        a = HeronaBrahmagupty.dlugosc(point1, point2)
        b = HeronaBrahmagupty.dlugosc(point2, point3)
        c = HeronaBrahmagupty.dlugosc(point3, point1)
        ob = HeronaBrahmagupty.obwodTr(point1, point2, point3)
        p = ob/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)
    
    @staticmethod
    def Brahmagupty(point1, point2, point3, point4):
        a = HeronaBrahmagupty.dlugosc(point1, point2)
        b = HeronaBrahmagupty.dlugosc(point2, point3)
        c = HeronaBrahmagupty.dlugosc(point3, point4)
        d = HeronaBrahmagupty.dlugosc(point4, point1)
        ob = HeronaBrahmagupty.obwodCz(point1, point2, point3, point4)
        p = ob/2
        return ((p-a)*(p-b)*(p-c)*(p-d))**(1/2)
    

point1 = Point(0, 0)
point2 = Point(2, 0)
point3 = Point(2, 2)
point4 = Point(0, 2)

print(HeronaBrahmagupty.obwodTr(point1, point2, point3))
print(HeronaBrahmagupty.obwodCz(point1, point2, point3, point4))
print(HeronaBrahmagupty.Heron(point1, point2, point3))
print(HeronaBrahmagupty.Brahmagupty(point1, point2, point3, point4))

#4
print('Zadanie 4')
class Counter:
    count = {}

    def __init__(self, fun):
        self._fun = fun
        Counter.count[self] = 0

    def __call__(self, *p):
        Counter.count[self] += 1
        return self._fun(*p)

    @staticmethod
    def getCount(fun):
        return Counter.count[fun]

@Counter
def test():
    return 0

@Counter
def test2(a, *b):
    return 0

test()
print(Counter.getCount(test))

test()
print(Counter.getCount(test))

test2(1, [2,])
print(Counter.getCount(test2))

test2(1, [2,])
print(Counter.getCount(test2))

f = test2
f(1, [2,])
print(Counter.getCount(test2))
print(Counter.getCount(f))