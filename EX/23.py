import sys
import math
from functools import cache

input = sys.stdin.read

def solve():
  N = int(input())
  if not N:
      return
  
  @cache
  def f(n):
    if n == 0:
        return 1
    if n >= 1:
      return f(math.floor(n/2)) + f(math.floor(n/3)) + f(math.floor(n/5))
      
  print(f(N))

if __name__ == "__main__":
  solve()
