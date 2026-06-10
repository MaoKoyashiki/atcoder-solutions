import sys
from sortedcontainers import SortedSet
input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
  L = int(lines[0])
  Q = int(lines[1])
  c = lines[2::2]
  c = list(map(int, c))
  x = lines[3::2]
  x = list(map(int, x))
  x1 = SortedSet([])

  for i in range(len(c)):
    if c[i] == 1:
      x1.add(x[i])
    if c[i] == 2:
      diff = 0
      z = 0
      z = x1.bisect_left(x[i]) - 1
      if z == -1:
        diff += x[i]
      else:
        diff += x[i] - x1[z]
      if z + 1 == len(x1):
        diff += L - x[i]
        print(diff)
        continue
      diff += x1[z+1] - x[i]
      print(diff)
      
if __name__ == "__main__":
  solve()