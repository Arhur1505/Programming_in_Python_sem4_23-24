import time
import sys
import math
import random

#1
print('Zadanie 1')
powt=1000
N=10000

def forStatement():
    result = []
    for i in range(N):
       result.append(i)
    #  result.append(i**2)
    sum1 = 0
    for j in result:
        sum1+=1
    return result

def listComprehension():
    result = [i for i in range(N)]
    #result = [i**2 for i in range(N)]
    sum1 = 0
    for j in result:
        sum1+=1
    return result

def mapFunction():
    result = map(lambda i: i, range(N))
    #result = map(lambda i: i**2, range(N))
    #result = list(result) 
    sum1 = 0
    for j in result:
        sum1+=1
    return result

def generatorExpression():
    result = (i for i in range(N))
    #result = (i**2 for i in range(N))
    #result = list(result) 
    sum1 = 0
    for j in result:
        sum1+=1
    return result
        
def tester(function):
    start = time.time_ns()

    for _ in range(powt):
        function()


    stop = time.time_ns()
    return (stop - start)        

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))



#2
print('Zadanie 2')
N = 100000
lista = list(filter(lambda x: x[0]**2+x[1]**2<1, ((random.uniform(-1,1), random.uniform(-1,1)) for i in range(N))))
c = len(lista)

print('pi = ', c*4/N)

#3
print('Zadanie 3')
def fun3(x, y):
    n = len(x)
    xa = sum(x)/n
    ya = sum(y)/n
    D = sum(map(lambda xi: (xi-xa)**2, x))
    a = sum(map(lambda xi, yj: yj*(xi-xa), x, y))/D
    b = ya-a*xa
    yd = math.sqrt(sum(map(lambda xi, yj: (yj-a*xi-b)**2, x, y))/(n-2))
    ad = yd/math.sqrt(D)
    bd = yd*math.sqrt(1/n+xa**2/D)
    return a, b, ad, bd

a, b, ad, bd = fun3(list(range(10)),[2*i+7+random.uniform(-0.1,0.1) for i in range(10)])
print(a, b, ad, bd)


#4
print('Zadanie 4')
def myreduce(fun, seq):
    result = seq[0]
    for i in seq[1:]:
        result = fun(result, i)
    return result

seq = [1, 2, 3, 4, 5, 6]
print(myreduce(lambda x,y: x+y, seq))
print(myreduce(lambda x,y: x*y, seq))


#5
print('Zadanie 5')
m1 = [[11,15,2], [19,56,93], [13,72,20]]

mr = list(map(max, m1))
print(mr)

mc = list(map(max, zip(*m1)))
print(mc)

m2 = [[1,2,3], [1,2,3], [1,2,3]]
m3 = [[1,2,3], [1,2,3], [1,2,3]]

adding_matrixes = lambda *matrixes: [[sum(values) for values in zip(*rows)] for rows in zip(*matrixes)]
sum_m = adding_matrixes(m1, m2, m3)
print(sum_m)