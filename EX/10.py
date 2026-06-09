# EX10 - 平均との差 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cm
N = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(N):
  sum += a[i]
  
mean = sum // N

for i in range(N):
  print(abs(a[i] - mean))