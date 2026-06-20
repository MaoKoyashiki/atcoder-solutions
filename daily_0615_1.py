import sys

def solve():
    input_data = sys.stdin.read.split()
    if not input_data:
        return

    S = input_data[0]
    T = input_data[1]

    n = len(s)

    for w in range(1, n):
        for c in range(1, w + 1):
            extracted = S[c-1::w]

        if extracted == T:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    solve()