import sys

#1
if len(sys.argv) < 2:
    print("Przy wykonaniu programu musisz dodać argumenty po nazwie")
    sys.exit()
else:
    arguments = ' '.join(sys.argv[1:])

#2
small_letters = [a for a in arguments if a.islower()]
capital_letters = [a for a in arguments if a.isupper()]
numbers = [a for a in arguments if a.isnumeric()]
digits = [a for a in arguments if a.isdigit()]

#3
unique_small_letters = []
for letter in small_letters:
    if letter not in unique_small_letters:
        unique_small_letters.append(letter)

new_small_letters = [(i, small_letters.count(i)) for i in unique_small_letters]

#4
sorted_list = sorted(new_small_letters, key=lambda x: x[1], reverse=True)

#5
a = sum(1 for char in arguments if char.lower() in 'aeiouyAEIOUY')
b = sum(1 for char in arguments if char.isalpha() - a)
print(a, b)

values = [(int(number), a * int(number) + b) for number in numbers]
print(values)

#6
import math
x = sum(number for number, _ in values) / len(values) 
y = sum(value for _, value in values) / len(values) 
D = sum((number - x) ** 2 for number, _ in values)

a = sum(value * (number - x) for number, value in values)/D
b = y - a*x

print(a, b)