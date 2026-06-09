import sys
from math import cos, pi, sqrt, radians

input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
    
  A = int(lines[0])
  B = int(lines[1])
  H = int(lines[2])
  M = int(lines[3])
  
  h = 30 * H + 30 * M / 60
  m = 6 * M
  d = abs(h - m)
  theta = min(d, abs(360 - d))
  s = float(A ** 2) + float(B ** 2) - 2 * A * B * cos(radians(theta))

  print(sqrt(s))
  
if __name__ == "__main__":
  solve()

  