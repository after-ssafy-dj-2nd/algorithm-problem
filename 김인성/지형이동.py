from heapq import heappush, heappop

def solution(land, height):
    n = len(land)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    area = [[0]*n for _ in range(n)]
    not_used = {(i, j):True for i in range(n) for j in range(n)}
    now = 0
    while not_used:
        stack = [not_used.popitem()[0]]
        while stack:
            x0, y0 = stack.pop()
            area[y0][x0] = now
            h = land[y0][x0]
            for i in range(4):
                x, y = x0 + dx[i], y0 + dy[i]
                if not_used.get((x, y)) and abs(land[y][x] - h) <= height:
                    stack.append((x, y))
                    not_used.pop((x, y))
                    area[y][x] = now
        now += 1
    graph = {i:{} for i in range(now)}
    for j0 in range(n):
        for i0 in range(n):
            for k in range(2):
                i, j = i0 + dx[k], j0 + dy[k]
                if i < n and j < n:
                    a1, a2 = area[j0][i0], area[j][i]
                    if a1 != a2:
                        try:
                            graph[a1][a2] = graph[a2][a1] = min(graph[a1][a2], abs(land[j0][i0] - land[j][i]))
                        except KeyError:
                            graph[a1].update({a2: abs(land[j0][i0] - land[j][i])})
                            graph[a2].update({a1: abs(land[j0][i0] - land[j][i])})
    Inf = 0xffff
    ans = cnt = 0
    prim = [Inf] * now
    heap = [(0, 0)]
    while heap and cnt < now:
        dist, index = heappop(heap)
        if prim[index] == Inf:
            prim[index] = dist
            cnt += 1
            ans += dist
            for idx, val in graph[index].items():
                if prim[idx] == Inf:
                    heappush(heap, (val, idx))
    return sum(prim)