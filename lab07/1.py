import math
import sys
import random

#1
print('Zadanie 1:')

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


def perfect_numbers(sequence):
    for num in sequence:
        divisor = sum(divisor for divisor in range(1, num) if num % divisor == 0)
        if divisor == num:
            yield num

def sequence(seq, max_value):
    for num in seq:
     if num > max_value:
         break
     yield num        

for num in perfect_numbers(sequence(natural_numbers(), 10000)):
    print(num)

#2
print('Zadanie 2:')

def natural_log(a, x_max):
    u0 = 0  
    x0 = 1
    i = 0       
    while x0 <= x_max:
        yield x0, u0, math.log(x0)
        i += 1
        x0 += a
        u0 = u0 + a/x0

a = 0.05
x_max = 1.5
for x, ln, true_ln in natural_log(a, x_max):
    print(x, ln, true_ln)

#3
print('Zadanie 3:')

def sin(x, error):
    k = 0
    a = x
    sin_sum = a
    while abs(a) > error:
        k += 1
        a *= -1 * x**2 / ((2 * k) * (2 * k + 1)) 
        sin_sum += a
        yield sin_sum, k

#4
print('Zadanie 4:')

def real_range(*args):
    arg = len(args)
    if arg == 1:
        start, stop, step = 0, args[0], 1
    elif arg == 2:
        start, stop, step = args[0], args[1], 1
    elif arg == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        print("Błędna ilość argumentów")
    

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

print(list(real_range(10,1,-2)))
print(list(range(10,1,-2)))

#5
print('Zadanie 5:')

def generate():
    current = random.uniform(0,1)
    yield current

    while True:
        next_value = random.uniform(0,1)
        while abs(next_value - current) < 0.4:
            next_value = random.uniform(0,1)
        if next_value < 0.1:
            break

        yield next_value
        current = next_value

for num in generate():
    print(num)
