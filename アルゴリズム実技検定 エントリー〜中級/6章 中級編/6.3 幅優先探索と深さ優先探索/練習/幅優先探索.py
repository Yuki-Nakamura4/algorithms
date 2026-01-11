# 間違えまくった箇所・注意点をコメントで示す

from collections import deque

# アンパック代入。リストの中身を左辺の変数にそれぞれ代入できる。変数の数とリストの長さが合わないとエラー
R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

B = []

for i in range(R):
    row = list(
        input()
    )  # 文字列なのでリストに変換。スペースのない単なる文字列なのでsplit()もしない
    B.append(row)

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = [
    [-1] * C for _ in range(R)
]  # [[-1]*C]*R は不可。同じリストへの参照が複製されてしまう

Q = deque()
Q.append((sy, sx))
dist[sy][sx] = 0

visited = [[False] * C for _ in range(R)]
visited[sy][sx] = True  # スタートを訪問済みにするのを忘れない

while len(Q) > 0:
    i, j = Q.popleft()
    for i2, j2 in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        if 0 <= i2 < R and 0 <= j2 < C:
            if B[i2][j2] == "." and not visited[i2][j2]:
                visited[i2][j2] = True
                dist[i2][j2] = dist[i][j] + 1
                if i2 == gy and j2 == gx:
                    print(dist[i2][j2])
                    exit()
                Q.append((i2, j2))
