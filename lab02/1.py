#1
print('Zadanie 1:')
k=[8,0,17,1,10,13,13,13,10,3,]
for i in range(k.count(13)):
    k.remove(13)
print(k)

#2
print('Zadanie 2:')
k=[8,0,17,1,10,13,13,13,10,3,]
while k.count(13):
    k.remove(13)
print(k)

k=[8,0,17,1,10,13,13,13,10,3,]
while 13 in k:
    k.remove(13)
print(k)

#3
print('Zadanie 3:')
k=[8,0,17,1,10,13,13,13,10,3,]
for i in range(1, len(k), 2):
    print(k[i], end=', ')
print(' ')
#4
print('Zadanie 4:')
k=[8,0,17,1,10,13,13,13,10,3,]
print(k[1::2])

#5
print('Zadanie 5:')
k=[8,0,17,1,10,13,13,13,10,3,]
for i in range(len(k), 0, -2):
    print(k[i-1], end=', ')
print(' ')

#6
print('Zadanie 6:')
k=[8,0,17,1,10,13,13,13,10,3,]
print(k[::-2])

#7
print('Zadanie 7:')
k=[8,0,17,1,10,13,13,13,10,3,]
l=[(i, k[i]) for i in range(len(k))]
print(l)

#8
print('Zadanie 8:')
l.sort(key=lambda x: x[1])
print(l)

#9
print('Zadanie 9:')
k=[8,0,17,1,10,13,13,13,10,3,]
l=[]
l=[(i, k[i]) for i in range(len(k)) if not k[i]%2]
print(l)

#10
print('Zadanie 10:')
k=[8,0,17,1,10,13,13,13,10,3,]
l=[]
l=[(i, k[i]) if k[i]>i else (k[i], i) for i in range(len(k))]
print(l)

#11
print('Zadanie 11:')
k=[[] for i in range(10)]
k[3].append(1)
print(k)