from random import *
import time
seed()
MAX_J = 1000
MAX_I = 10000
total = 0.0
tl = time.time()
for j in range(MAX_J):
    score = 0.0
    for i in range(MAX_I):
        x = random()
        y = random()
        r = x*x+y*y
        if r < 1:
            score += 1
    score = 4*score/MAX_I
#    print(score)
    total += score
print()
t = time.time()-tl
print(total/MAX_J)
print('計算時間:', t, '秒')
