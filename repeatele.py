su=int(input())
lis=[]
l=""
for i in range(su):
    a=input()
    lis.append(a)
co=0
li1=[]
for j in lis:
    cou=0
    if co==0:
        l+=j
        co+=1
    else:
        for k in range(10):
            if j[:(len(j)-cou)] in l:
                l+=(j[:(len(j)-cou)])
                li1.append(len(j[:(len(j)-cou)]))
                break
            else:
                cou+=1
aaa=min(li1)
print(l[:aaa])
