s,u=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(u):
    b,c=list(map(int,input().split()))
    print(min(a[(b-1):(c)]))
