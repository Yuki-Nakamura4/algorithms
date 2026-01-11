import sys

sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
C = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            sy, sx = i, j
        if C[i][j] == "g":
            gy, gx = i, j

visited = [[False] * W for _ in range(H)]


def dfs(i, j):
    visited[i][j] = True

    for i2, j2 in [(i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j)]:
        if not 0 <= i2 < H or not 0 <= j2 < W:
            continue
        if C[i2][j2] == "#":
            continue
        if visited[i2][j2]:
            continue
        dfs(i2, j2)


dfs(sy, sx)

print("Yes" if visited[gy][gx] else "No")
