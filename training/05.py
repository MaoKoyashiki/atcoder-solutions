# code 5-1
N = 7
h = [2, 9, 4, 5, 1, 6, 10]
dp = [0 for _ in range(N)]
choice = []
c = []
for i in range(1, N):
    if i == 1:
        dp[i] = abs(h[i] - h[i-1])
        choice.append(1)
        continue
    dp[i] = min((dp[i-1] + abs(h[i] - h[i-1])), (dp[i-2] + abs(h[i] - h[i-2])))
    if dp[i] - dp[i-1] == abs(h[i] - h[i-1]):
        choice.append(1)
    else:
        choice.append(2)
i = N - 2
while i > 0:
    c.append(choice[i])
    i -= choice[i]
print(dp[N-1])
c.reverse()
print(c)

# 5.1
# vacation C
N = 5
A = [3, 2, 4, 5, 1]
B = [2, 5, 1, 3, 4]
C = [3, 1, 5, 2, 5]
# dp = [[0 for _ in range(N)] * 3]
dp = [[0 for _ in range(N)] for _ in range(3)]
for i in range(N):
  if i == 0:
    dp[0][0] = A[0]
    dp[1][0] = B[0]
    dp[2][0] = C[0]
    continue
  # i日目にAを選ぶ
  # i-1日目にBorC
  dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + A[i]
  
  # i日目にBを選ぶ
  # i-1日目にAorC
  dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + B[i]
  
  # i日目にCを選ぶ
  # i-1日目にAorB
  dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + C[i]
  
print(max(dp[0][4], dp[1][4], dp[2][4]))

# 5.2
# 部分和問題
A = [1, 7, 3, 5, 2]
N = len(A)
W = 15
dp = [[False for _ in range(W+1)] for _ in range(N)]
for i in range(N):
  dp[i][0] = True
# --- n=0 (最初の要素) の初期化 ---
if A[0] <= W:
    dp[0][A[0]] = True
# --- n=1 (2番目の要素) 以降のループ ---
for n in range(1, N):
  for w in range(W+1):
    # 1. まず「選ばない場合」の結果をそのまま引き継ぐ
    dp[n][w] = dp[n-1][w]
    # 2. 「選ぶ場合」のチェック（w が A[n] 以上のときだけ引ける）
    if w >= A[n]:
      # すでに True ならそのまま、False なら「A[n]を足す前の状態」を引き継ぐ
      dp[n][w] = dp[n][w] or dp[n-1][w - A[n]]
for i in range(N):
  print(dp[i][W])

  