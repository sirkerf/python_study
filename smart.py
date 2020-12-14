def solve():
    rem = N
    prev = 0

    for _ in range(M):
        a, b = map(int, input().split())
        rem -= a - prev

        if rem <= 0:
            return False
        rem += b - a
        rem = min(N,rem)
        prev = b

    rem -= (T - prev)
    if rem <= 0:
        return False
    return True

N, M, T = map(int, input().split())

if solve():
    print("Yes")
else:
    print("No")