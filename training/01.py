import sys

def solve():
    # 入力をすべて高速に読み込む
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = int(input_data[1])
    K = int(input_data[2])
    # A_1, A_2, ..., A_N の切れ目の位置
    A = [int(x) for x in input_data[3:3+N]]
    
    # --- 1. 判定関数 ---
    # 「すべてのピースの長さを x 以上にしつつ、K回以上切れるか？」を判定
    def check(x):
        cut_count = 0
        last_cut = 0  # 前回の切れ目の位置（最初は左端の0）
        
        for i in range(N):
            # 現在の切れ目までの長さが x 以上になったら切る
            if A[i] - last_cut >= x:
                cut_count += 1
                last_cut = A[i]
        
        # 最後の切れ目から右端（L）までの長さも x 以上である必要がある
        # かつ、切った回数が K 回以上であれば条件達成
        return cut_count >= K and (L - last_cut) >= x

    # --- 2. 答えの値で二分探索 ---
    left = 1
    right = L
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if check(mid):
            ans = mid       # mid以上のスコアが作れたので記録
            left = mid + 1  # もっと大きなスコaを目指して右側を探索
        else:
            right = mid - 1 # 大きすぎたので左側を探索
            
    print(ans)

if __name__ == '__main__':
    solve()