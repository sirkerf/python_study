s=input()
a=["maerd","remaerd","esare","resare"]
d,k="",""
n=len(s)
for i in range(1,n+1):
    k+=s[-i]
i=0
while i<=n:
    if k[i:i+5]==a[0]:
        d+=a[0]
        i+=5
    elif k[i:i+7]==a[1]:
        d+=a[1]
        i+=7
    elif k[i:i+5]==a[2]:
        d+=a[2]
        i+=5
    elif k[i:i+6]==a[3]:
        d+=a[3]
        i+=6
    else:
        break
if k==d:
    print("YES")
else:
    print("NO")