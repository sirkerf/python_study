n, m = map(int, input().split())
a = [0] + list(map(int, input().split())) + [n + 1]
a.sort()

b = []
for i, j in zip(a, a[1:]):
    if j - i != 1:
        b.append(j - i - 1)

if not b:
    print(0)
    exit()

k = min(b)
ans = 0
for i in b:
    ans += -(-i // k)
print(ans)