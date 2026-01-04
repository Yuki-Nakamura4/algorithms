import sys
import heapq


def dijkstra(n: int, g: list[list[tuple[int, int]]], start: int) -> list[int]:
    """最短経路を求めるダイクストラのアルゴリズム。
    最小の重みの点を探し、隣接するすべての点に対してその点の重み+経路の重みが行き先の重みより小さければ更新するという処理を繰り返す。
    最小の重みが終点になったら終了する。

    Args:
        n (int): 頂点数
        g (list[list[tuple[int, int]]]): グラフの隣接リスト表現。g[v]は頂点vに隣接する(行き先, 重み)の組のリスト
        start (int): 始点の頂点番号(0-index)

    Returns:
        list[int]: 各頂点への最短距離のリスト
    """

    INF = 10**18  # 到達不能な頂点の距離を表す値
    dist = [INF] * n  # 各頂点への最短距離を格納する配列
    dist[start] = 0  # 始点を表す距離。0で固定

    # 優先度付きキュー(最小ヒープ)
    # (距離, 頂点) を入れておくと距離が最小の候補から順に取り出せる
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)  # 現在の最短距離とその頂点

        # pqにはdist[v] が更新された後も更新前の(d, v)が残ってしまう
        # それを弾くため、今の最短距離と一致しないものは無視する
        if d != dist[v]:
            continue

        # 頂点vに隣接する各頂点について
        for to, w in g[v]:
            nd = d + w  # vを経由してtoに行く場合の距離

            # その頂点の現在の最短距離よりも小さければ更新
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))

    return dist


# 計算量: O((E + V) log V)
# - E: 辺の本数
# - V: 頂点の本数
# - 各頂点が優先度付きキューに入るのは最大で1回
# - 各辺に対して緩和処理を行うため、全体の計算量は O((E + V) log V)


def main() -> None:
    input = sys.stdin.readline

    # n, m, s: 頂点数、辺数、始点
    n, m, s = map(int, input().split())
    s -= 1  # 0-indexへ

    # グラフの隣接リスト表現。
    # g[v]は頂点vに隣接する(行き先, 重み)の組のリスト
    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        a -= 1  # 0-indexへ
        b -= 1

        # 無向なので両方向
        g[a].append((b, w))
        g[b].append((a, w))  # 有向の場合はこの行をコメントアウト

    dist = dijkstra(n, g, s)

    # 出力例: 到達不能は-1にする
    INF = 10**18
    for d in dist:
        # 各頂点への最短距離を出力
        print(-1 if d == INF else d)


if __name__ == "__main__":
    main()

# 問題例
# 問題:
# N頂点M辺の連結とは限らない無向重み付きグラフが与えられる。各辺の重みは0以上の整数。始点Sから各頂点への最短距離を求めよ。到達不可能な頂点は-1を出力せよ。
# 入力:
# 1行目: N M S
# 続くM行: A_i B_i W_i (頂点A_iとB_iを結ぶ重みW_iの無向辺)
# 制約(例):
# 1 ≤ N ≤ 2×10^5
# 0 ≤ M ≤ 2×10^5
# 1 ≤ S ≤ N
# 0 ≤ W_i ≤ 10^9
# 出力:
# 頂点1..Nについて、Sからの最短距離を各行に出力。到達不能なら-1。


def dijkstra_to_target(
    n: int,
    g: list[list[tuple[int, int]]],
    start: int,
    target: int,
) -> int:
    """特定の頂点への最短距離を求めたい場合のダイクストラ法。"""
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d != dist[v]:
            continue

        if v == target:
            return d  # ここで最短距離が確定

        for to, w in g[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))

    return -1  # targetへ到達不能
