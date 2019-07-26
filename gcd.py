import math
su=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(su[1]):
    b,c=list(map(int,input().split()))
    print(math.gcd(a[b-1],a[c-1]))
