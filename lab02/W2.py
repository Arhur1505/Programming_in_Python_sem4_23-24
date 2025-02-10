k=[8,0,17,1,10,13,19,13,10,3,]
np=[i for i in k if i%2]
print(np)
np=[i if i>0 else -1 for i in k]
print(np)

k=[(k[i],k[-i-1]) for i in range(len(k)//2)]
print(k)

N=3
k=[]
for i in range(N):
    tmp=[]
    for j in range(N):
        tmp.append((i,j))
    k.append(tmp)
print(k)

k, tmp=[], []
for i in range(N):
    for j in range(N):
        tmp.append((i,j))
    k.append(tmp)
    tmp.clear()
print(k)

k=[[(i,j) for j in range(N)] for i in range(N)]
print(k)