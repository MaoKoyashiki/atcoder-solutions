import sys

input = sys.stdin.read

def solve():
  lines = input().split()
  if not lines:
      return
  N = int(lines[0])
  A = lines[1:1+N]
  A = list(map(int, A))
  B = lines[1+N:]
  B = list(map(int, B))
  flag = True
  for i in range(len(A)):
    if i + 1 != B[A[i]-1]:
      flag = False
  
  if flag:
    print("Yes")
  else:
    print("No")
  
if __name__ == "__main__":
  solve()