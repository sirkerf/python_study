from math import comb

L = int(input())
X = L - 12
ans = comb(X + 11, 11)
print(ans)