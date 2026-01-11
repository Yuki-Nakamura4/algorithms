import sys
from assets.lib.union_find import UnionFind


def kruskal() -> None:
    """最小全域木(MST)を求めるクラスカルのアルゴリズム。"""
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append(
            (w, u, v)
        )  # (重み, 端点u, 端点v)。重みでソートしやすいように順番を入れ替える

    # 辺を重みの昇順にソート
    edges.sort()

    uf = UnionFind(n)
    mst_cost = 0  # 最小全域木のコスト
    used_edges = 0  # 最小全域木に採用した辺の本数(木の性質から必ずn-1本になる)

    # 軽い辺から順にサイクルにならないなら採用
    for w, u, v in edges:
        if uf.unite(u, v):  # 既に連結ならFalseが返る
            mst_cost += w
            used_edges += 1
            # 木の性質から、最小全域木の辺の本数は必ず n-1 本になる
            if used_edges == n - 1:
                break

    # 連結でない場合は最小全域森のコストが出る
    print(f"mst_cost: {mst_cost}")


if __name__ == "__main__":
    kruskal()

# 計算量: O(M log M) --- IGNORE ---
# - M: 辺の本数
# - 辺のソートに O(M log M)
# - 各辺に対する Union-Find の操作にほぼ定数時間
# 定数時間なのは、Union-Find の各操作が逆アッカーマン関数 α(n) に比例するため。α(n) は n が現実的な大きさであれば最大でも 4 以下になる非常に遅く増加する関数であるため、ほぼ定数時間とみなせる。
# よって、全体の計算量は O(M log M)

S = input()
ans = set()

for k in range(1, 4):
    for i in range(len(S)):
        if i + k > len(S):
            continue

        sub = S[i : i + k]

        for mask in range(1 << k):
            list_sub = list(sub)
            for j in range(k):
                if mask & 1 << j:  # &はビット演算のときのみ使う
                    list_sub[j] = "."
            ans.add("".join(list_sub))

print(len(ans))
