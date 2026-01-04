T = int(input())
N = int(input())
L, R = [None]*N,  [None]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())

diff = [0]*(T+1)

for i in range(N):
    diff[L[i]] += 1
    diff[R[i]] -= 1

cum = [0]*(T+1)
cum[0] = diff[0] # 0時に来る従業員の数を忘れないようにする

for t in range(1, T+1):
    # cumはその時間からの従業員が来て、その時間で終わりの従業員が帰った直後(t時直後)の従業員数を表す
    cum[t] = diff[t] + cum[t-1]

for t in range(T):
    print(cum[t]) 