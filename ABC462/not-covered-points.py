import sys
import math

input = sys.stdin.readline

def solve():
  N = int(input())
  xy = []
  count = 0
  for i in range(N):
    x, y = map(int, input().split())
    xy.append((x - 1, y - 1))
  xy.sort()
  x_min = xy[0][0]
  y_min = N + 1
  for i in range(N):
    x = xy[i][0]
    y = xy[i][1]
    if  y <= y_min:
      y_min = y
      count += 1
  print(count)
if __name__ == "__main__":
  solve()