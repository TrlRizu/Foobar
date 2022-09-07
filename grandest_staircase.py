import random
import time
import matplotlib.pyplot as plt

def answer(n):
    m = [[0 for i in range(n + 2)] for i in range(n + 2)]
    return solve(1, n, m) - 1

def solve(h, l, m):
    if m[h][l] != 0:   
        return m[h][l]
    if l == 0:
        return 1
    if l < h:
        return 0
    m[h][l] = solve(h + 1, l - h, m) + solve(h + 1, l, m)
    return m[h][l]


#For testing
ans = []
y = []
start = time.time()
for i in range(201):
    x = answer(i)
    n = y.append(i)
    ans.append(x)
    end = time.time()
    total_time = end - start

# print(ans)
# print(y)

plt.plot(ans, y, color='green', markersize=12)
plt.xlabel('answer(n)')
plt.ylabel('Numbers')
print("Time taken: "+ str(total_time))
plt.show()

