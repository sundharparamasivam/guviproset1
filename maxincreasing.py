su=int(input())
a=list(map(int,input().split()))
j=-1
k=0
c=1
l1=[]
for i in range(1,len(a)):
    j+=1
    k+=1
    if a[j]<=a[k]:
        c+=1
    else:
        l1.append(c)
        c=1
print(min(l1))
