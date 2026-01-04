import heapq


def dijkstra(n, graph, start):
    INF = 10000 * 18
    dist = [INF] * n

    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        if d != dist[v]:
            continue

        for to, w in graph[v]:
            nd = d + w

            if nd < dist[v]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))

    return dist
