import sys
sys.setrecursionlimit(10**6)
from math import cos, pi, sqrt, radians

input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
    
  N = int(lines[0])
  
  def f(n):
    if n == 0:
      return 0
    cnt = popcount(n)
    if cnt % 2 == 1:
      return f(n - 1) + 1
    else:
      return f(n - 2) + 1
    
  def popcount(x):
    count = 0
    while x > 0:
      # 下1ケタ（最下位ビット）を取り出す
      if x & 1:
        count += 1
    
      # 処理が終わったら、右に1ビットシフト（一つ左の桁を次に調べる準備）
      x = x >> 1
      
    return count
    
  print(f(N))
  
if __name__ == "__main__":
  solve()

  