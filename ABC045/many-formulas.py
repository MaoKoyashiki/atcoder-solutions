# AtCoder Beginner Contest 045 - C: Many Formulas
# URL: https://atcoder.jp/contests/abc045/tasks/arc061_a
# 計算量: O(N * 2^(N-1))
# ポイントはbit全探索で部分集合を全て列挙することです。
# これはO(2^(N-1))で列挙できます。
# その後、部分集合の和を計算して、countに加算します。
# これはO(N)で計算できます。
# したがって、計算量はO(N * 2^(N-1))です。
N = "125"
n = len(N)
def solve():
    count = 0
    for i in range(1 << (n-1)):
        current_str = N[0]
        current_sum = 0
        for j in range(n-1):
            if not (i & (1 << j)):
                current_str += N[j+1]
            else:
                current_sum += int(current_str)
                current_str = N[j+1]
        current_sum += int(current_str)
        count += current_sum
    return count

if __name__ == "__main__":
    print(solve())
