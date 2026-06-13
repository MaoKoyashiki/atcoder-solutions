N = int(input())
ans = [[] for _ in range(N+1)]
for i in range(N):
  line = input().split()
  K = list(map(int, line[1:]))
  for j in K:
    ans[j].append(i+1)
  
for i in range(1, N+1):
  print(len(ans[i]), *ans[i])

##################################
# 解説
n = int(input())
ans = [[] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))[1:]
    for c in a:
        ans[c - 1].append(i + 1)
for i in range(n):
    a = [len(ans[i])] + ans[i]
    print(*a)
