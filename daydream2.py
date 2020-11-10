S = input()
S = S[::-1]
 
flag = False
while(True):
    if S == "":
        flag = True
        break
 
    if S.startswith("remaerd"):
        S = S[7:]
        continue
 
    if S.startswith("resare"):
        S = S[6:]
        continue
 
    if S.startswith("maerd"):
        S = S[5:]
        continue
 
    if S.startswith("esare"):
        S = S[5:]
        continue
    
    break
 
if flag:
    print("YES")
else:
    print("NO")