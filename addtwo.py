su=int(input())
a=list(map(int,input().split()))
a=sorted(a)
b=a[::-1]
print(sum(b[:2]))
