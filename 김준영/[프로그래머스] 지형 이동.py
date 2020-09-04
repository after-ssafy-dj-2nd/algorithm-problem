import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    cnt = 1
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                bfs(visit, land, height, n, cnt, i, j)
                cnt += 1
    G = findconnect(visit, cnt, land)
    answer = prim(G, cnt)

    return answer

def bfs(visit, board, h, w, c, x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]
    visit[x][y] = c
    stack = [(x, y)]
    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if -1 < tx < w and -1 < ty < w and not visit[tx][ty] and abs(board[tx][ty] - board[x][y]) <= h:
                visit[tx][ty] = c
                stack.append((tx, ty))

def findconnect(visit, c, board):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    G = [[] for _ in range(c)]
    w = dict()
    for i in range(len(visit)):
        for j in range(len(visit)):
            for k in range(4):
                tx, ty = i + dx[k], j + dy[k]
                if -1 < tx < len(visit) and -1 < ty < len(visit) and visit[tx][ty] != visit[i][j]:
                    if w.get((visit[tx][ty], visit[i][j])):
                        if w[(visit[tx][ty], visit[i][j])] > abs(board[tx][ty] - board[i][j]):
                            w[(visit[tx][ty], visit[i][j])] = abs(board[tx][ty] - board[i][j])
                    else:
                        w[(visit[tx][ty], visit[i][j])] = abs(board[tx][ty] - board[i][j])
    for key in w:
        x, y = key
        G[x].append((y, w[key]))
    return G

def prim(G, c):
    D = [1e9] * c
    visit = [0] * c
    cnt = c
    D[1] = 0
    h = [(0, 1)]
    heapq.heapify(h)

    while h:

        MIN, u = heapq.heappop(h)
        if MIN > D[u]: continue
        visit[u] = 1

        for g in G[u]:
            e, w = g
            if not visit[e] and  w < D[e]:
                D[e] = w
                heapq.heappush(h, ((w, e)))

    return sum(D[1:])


solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)