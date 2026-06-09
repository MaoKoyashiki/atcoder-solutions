import sys
from math import gcd

input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
  
  N = int(lines[0])
  A = lines[1:]
  A = list(map(int, A))
  ans = gcd(*A)
  print(ans)
if __name__ == "__main__":
  solve()