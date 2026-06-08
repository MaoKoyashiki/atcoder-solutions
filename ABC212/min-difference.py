import sys
from bisect import bisect_left

input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return

  N = int(lines[0])
  M = int(lines[1])
  A = lines[2:2 + N]
  A = list(map(int, A))
  B = lines[2 + N:]
  B = list(map(int, B))
  
  B.sort()

  ans = 10000000000

  for a in A:
    idx = bisect_left(B, a)
    if idx < len(B):
        ans = min(ans, abs(B[idx] - a))
    if idx > 0:
      ans = min(ans, abs(B[idx - 1] - a))
  print(ans)
  
if __name__ == "__main__":
  solve()