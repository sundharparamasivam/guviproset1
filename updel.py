su=list(input().split())
x=su[0]
y=su[1]
c=0
for i in x:
    if i not in y:
        c+=1
for j in y:
    if j not in x:
        c+=1
print(c)
