import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
networks = {}
for _ in range(M):
    a, b = map(int, input().split())
    try:
        networks[a] += [b]
    except:
        networks[a] = [b]
    try:
        networks[b] += [a]
    except:
        networks[b] = [a]

kevin = [0]*(N+1)
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    Q = deque([(i, 0)])
    while len(Q) > 0:
        cur = Q.pop()
        curI = cur[0]
        curConnect = cur[1]
        kevin[i] += curConnect
        for n in networks[curI]:
            if visited[n] == 0:
                Q.appendleft((n, curConnect+1))
                visited[n] = 1

print(kevin.index(min(kevin[1:N+1])))