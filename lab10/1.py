import random
import matplotlib.pyplot as plt
import math

#1
print('Zadanie 1')

class IFS:
    def __init__(self, coefficients, probability):
        self.coefficients = coefficients
        self.probability = probability
        self.point = [(0,0)]

    def transform(self, iterations):
        for _ in range(iterations):
            p = random.choices(self.coefficients, self.probability)[0]
            a, b, c, d, e, f = p
            x, y = self.point[-1]
            self.point.append((a*x + b*y + c, d*x + e*y + f))

    def plot1(self, name):
        x_list, y_list = [], []
        for x, y in self.point:
            x_list.append(x)
            y_list.append(y)
        plt.figure()  
        plt.plot(x_list, y_list,'.')
        plt.savefig(name, format='png', dpi=300)
        print('Zapisano do pliku o nazwie ' + name)

ifs1 = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
ifs1.transform(5000)
ifs1.plot1('ifs1.png')

ifs2 = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)), (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
ifs2.transform(5000)
ifs2.plot1('ifs2.png')

ifs3 = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
ifs3.transform(5000)
ifs3.plot1('ifs3.png')


#2
print('Zadanie 2')

class Wektor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        return Wektor3D(self.x + a.x, self.y + a.y, self.z + a.z)
    
    def __sub__(self, a):
        return Wektor3D(self.x - a.x, self.y - a.y, self.z - a.z)
    
    def __mul__(self, a):
        return Wektor3D(self.x * a, self.y * a, self.z * a)
    
    def __str__(self):
        return f"Wektor: {self.x}, {self.y}, {self.z}"
    
    def skalarny(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def wektorowy(self, other):
        return Wektor3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def mieszany(self, vec_2, vec_3):
        return self.wektorowy(vec_2).skalarny(vec_3)
    
    def rozmiar(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
v1 = Wektor3D(1, 2, 3)
v2 = Wektor3D(1, 2, 3)
v3 = Wektor3D(1, 2, 3)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.skalarny(v2))
print(v1.wektorowy(v2))
print(v1.mieszany(v2, v3))
print(v1.rozmiar())

#3
print('Zadanie 3')
def strumien(B, S):
    return B.skalarny(S)

def sila(q, E, v, B):
    return E * q + (v.wektorowy(B)) * q

def praca(q, E, v):
    return q * E.skalarny(v)

B = Wektor3D(1, 2, 3)
S = Wektor3D(1, 2, 3)
E = Wektor3D(1, 2, 3)
v = Wektor3D(1, 2, 3)
q = 3


print(strumien(B, S))
print(sila(q, E, v, B))
print(praca(q, E, v))

