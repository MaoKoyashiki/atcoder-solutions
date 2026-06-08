# AtCoder Beginner Contest 253 - C: Max - Min Query
# URL: https://atcoder.jp/contests/abc253/tasks/abc253_c
# 毎回sortするとTLEするので、heapqとdictで高速化する
# 計算量: O(Q log Q)
# ポイントは出力用にheapqで最小値と最大値を管理することで、計算量を削減することです
# 辞書を使って個数を管理することで、O(1)で個数を取得できます。
# また、heapqと辞書が同期されていないのでカウントが0になった要素はheapqから削除する必要があります。
import sys
from heapq import heappop, heappush

# 入力の高速化（これを入れるとさらに速くなります）
input = sys.stdin.read


def solve():
    lines = input().split()
    if not lines:
        return

    Q = int(lines[0])

    # データの個数を管理する辞書
    counts = {}

    # 最小値と最大値を監視する2つのヒープ
    min_heap = []
    max_heap = []

    idx = 1
    for _ in range(Q):
        query_type = int(lines[idx])

        if query_type == 1:
            x = int(lines[idx + 1])
            idx += 2

            # 個数を増やす
            counts[x] = counts.get(x, 0) + 1
            # ヒープに追加
            heappush(min_heap, x) # logN
            heappush(max_heap, -x)  # 最大値はマイナスを入れて最小ヒープで代用 # logN

        elif query_type == 2:
            x = int(lines[idx + 1])
            c = int(lines[idx + 2])
            idx += 3

            if x in counts:
                # 削除する個数を決めて、辞書のカウントを減らす
                del_cnt = min(c, counts[x])
                counts[x] -= del_cnt
                if counts[x] == 0:
                    del counts[x]

        else:
            idx += 1

            # 最小値ヒープの先頭が、すでに削除されたゴミデータなら捨てる
            while min_heap and min_heap[0] not in counts:
                heappop(min_heap)

            # 最大値ヒープの先頭が、すでに削除されたゴミデータなら捨てる
            while max_heap and -max_heap[0] not in counts:
                heappop(max_heap)

            # 答えを出力（最大値 - 最小値）
            print(-max_heap[0] - min_heap[0])


if __name__ == "__main__":
    solve()