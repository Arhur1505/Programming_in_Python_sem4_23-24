import random
import sys
import string

#1
print('Zadanie 1')
def fun1(equ):
    d1 = {letter: str(random.randrange(0,10)) for letter in string.ascii_lowercase if letter != 'x'}
    d2 = str.maketrans(d1)
    equ = equ.translate(d2)

    result = [(x:=random.uniform(0,1), eval(equ)) for i in range(10)]

    return result

if len(sys.argv) < 2:
    sys.exit()

exp = (sys.argv[1])
print(fun1(exp))

#2
print('Zadanie 2')

def fun2(*args):
    common = []

    for item in args[0]:
        for other_items in args[1:]:
            if item not in other_items:
                break
        else:
            common.append(item)

    return common
tab1 = [1,2,3]
tab2 = (1,3,5)
tab3 = [3, 2, 1]

print(fun2(tab1, tab2, tab3))

#3
print('Zadanie 3')

def fun3(s1, s2, tr=True):
    if tr:
        return [(s1[i], s2[i]) for i in range(min(len(s1), len(s2)))]
    else:
        max1 = max(len(s1), len(s2))
        return [(s1[i] if i < len(s1) else None, s2[i] if i < len(s2) else None) for i in range(max1)]
    
s2 = [1, 2, 3, 4, 5, 6]
s1 = [6, 5, 4, 3, 2, 1, 0]

print(fun3(s1, s2, False))

#4
print('Zadanie 4')
def fun4(n):
    triangle = [[1]]
    for i in range(1, n+1):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)))

fun4(5)


#5
print('Zadanie 5')

def fun5(x, y, z, method = "r"):
    counter = 0

    while True:
        counter += 1

        if method == "r":
            temp = random.randint(y, z)
        else:
            temp = (y + z) // 2

        if x > temp:
            y = temp + 1
        elif x < temp:
            z = temp - 1
        else:
            return counter
        
print('Losując: ', fun5(15, 1, 100))
print('Dzieląc: ', fun5(15, 1, 100, 1))