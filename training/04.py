# 4.1
def tribonacci(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

# 4.2
N = 5
def tribonacci(n, memo):
    if n == 0 :
        return 0
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    if memo[n] != -1:
        return memo[n]
    memo = tribonacci(n-1, memo) + tribonacci(n-2, memo) + tribonacci(n-3, memo)
    return memo[n]

memo = [-1 for _ in range(N + 1)]
ans = tribonacci(N, memo)

# 4.5
# 答えをカウントする変数
# 計算量はO(3^d)
ans = 0
N = int(input())
def dfs(current_num):
    global ans
    # current_num が N を超えたら終了
    if current_num > N:
        return
    
    # 七五三数の条件判定
    s = str(current_num)
    if '3' in s and '5' in s and '7' in s:
        ans += 1
        
    # 次の桁を生成
    for next_digit in ['3', '5', '7']:
        dfs(current_num * 10 + int(next_digit))

# 初期値 0 からスタート
dfs(0)
print(ans)

# 4.6
N = 4
A = [3, 2, 6, 5]
w = 14
memo = [2 for _ in range(w)]
def subset_sum(w, memo):
    if w == 0:
        return 0
    if memo[w] != 2:
        return memo[w]
    for i in A:
        if i == w:
            return 1
    memo[w-1] = subset_sum(w-1, memo)
    return memo[w-1]
_ = subset_sum(w, A)
if memo[w] == 0:
    print("No")
if memo[w] == 1:
    print("Yes")

