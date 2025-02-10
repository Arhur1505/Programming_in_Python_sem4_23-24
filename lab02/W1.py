k=[8,0,17,1,10,13,19,13,10,3,]
for i in k:
    i*=2
    print(i, end=', ')

print('\n',k)

for i in range(len(k)):
    k[i]*=2

print(k)

for i, v in enumerate(k):
    k[i]=1 if v>0 else -1

print(k)

for i in k:
    if i%2:
        break
else:
    print('kiedy?')

k=[(89,34) , (92,31), (96,0), (48,30), (38,10),]

c=k[:]
c.sort()
print(c)

c=k[:]
c.sort(key=lambda x: x[1])
print(c)

c=k[:]
c.sort(reverse=True)
print(c)

k=[8,0,17,1,10,13,19,13,10,3,]
c=k[:]
c.sort(reverse=True)
print(c)