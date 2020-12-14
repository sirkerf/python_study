n,q=map(int,input().split())
a=list(map(int,input().split()))
bit=[0]*(n+1)
def add(i,x):
    i+=1
    while i<=n:
        bit[i]^=x
        i+=1&-i
def get(l,r):
    res=0
    while l:
        res^=bit[l]
        l-=l&-l
    while r:
        res^=bit[r]
        r-=r&-r
    return res
for i in range(n):add(i,a[i])
for _ in range(q):
    t,x,y=map(int,input().split())
    if t==1:add(x-1,y)
    else:print(get(x-1,y))