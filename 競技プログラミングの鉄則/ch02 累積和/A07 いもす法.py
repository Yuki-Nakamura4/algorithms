D = int(input())
N = int(input())
L, R = [None]*N,  [None]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 前日比の配列
B = [0] * (D+2) # 1日目をインデックス1にし、最終日翌日の累計参加者を0にする
for i in range(N):
    B[L[i]] += 1
    B[R[i] + 1] -= 1

# 累積和を計算
ans = [0] * (D+2)
for i in range(1, D+1):
    ans[i] = ans[i-1] + B[i]
    print(ans[i])