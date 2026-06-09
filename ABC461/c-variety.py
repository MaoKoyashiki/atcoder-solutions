import sys
from heapq import heappush, heapify, heappop
input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
  N = int(lines[0])
  K = int(lines[1])
  M = int(lines[2])
  A = lines[3:]
  A = list(map(int, A))
  v = [[] for i in range(N)]
  m = []
  n = []
  cnt = 0
  for i in range(0, len(A), 2):
    heappush(v[A[i]-1], -A[i+1])
  for i in range(N):
    if len(v[i]) == 0:
      continue
    m.append(v[i].pop(0))
  heapify(m)
  for i in range(M):
    cnt += heappop(m)
  for i in range(N):
    if len(v[i]) == 0:
      continue
    n.extend(v[i])
  n.extend(m)
  heapify(n)
  for i in range(K-M):
    cnt += heappop(n)
  print(-cnt)
  
if __name__ == "__main__":
  solve()
  