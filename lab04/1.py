import random
import string
import collections

#1
print('Zadanie 1')
k = 10
list1 = [random.randrange(0, 5*k) for i in range(k)]
d1 = collections.defaultdict(int)
for i in range(100):
    z = 0
    list2 = list1[:]
    random.shuffle(list2)
    for j in range(k):
        if list1[j] == list2[j]:
            z += 1
    d1[z]+=1 

print(d1)

#2
print('Zadanie 2')
k = 10
rstring = ".".join(random.sample(string.ascii_lowercase, k))
print(rstring)

#3
print('Zadanie 3')
list3 = [random.randrange(0, 20) for i in range(100)]
d2 = {}

for index, value in enumerate(list3):
    d2.setdefault(value, []).append(index)
d3 = {}
for i in list3:
    d3.setdefault(i, []).append(list3.index(i, d3[i][-1]+1 if d3[i] else 0))

print(d2)
print(d3)

#4
print('Zadanie 4')
palindrome = {n: sum(str(num) == str(num)[::-1] for num in [random.randint(10**(n-1), 10**n-1) for i in range(1000)]) for n in range(3,7)}
print(palindrome)

#5
print('Zadanie 5')
d4 = {i: random.randrange(1, 100) for i in range(10)}
print(d4)
d5 = {i: random.randrange(1, 100) for i in range(10)}
print(d5)

d4 = {value: key for key, value in d4.items()}
print(d4)
d5 = {value: key for key, value in d5.items()}
print(d5)

d6 = {i: (d4[i], d5[i]) for i in d4 if i in d5}
print(d6)