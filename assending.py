su=int(input())
l=[]
for i in range(su):
    a=list(map(int,input().split()))
    l.append(a)
l1=[]
for i in l:
    for j in i:
        l1.append(j)
l1=sorted(l1)
for i in l1:
    print(i,end=" ")
