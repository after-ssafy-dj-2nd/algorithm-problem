def isbuild(board, order, n):
    y, x, a, b = order
    x = n - x
    if a:  # 보
        # 한 쪽 끝이 기둥 위,
        if board[x][y][0][1] or board[x][y + 1][0][1] or (board[x][y][1][1] and board[x][y + 1][1][0]):
            return True
    else:  # 기둥
        # 바닥 위, 한 쪽 끝이 보 위, 기둥 위
        if x == n or board[x][y][1][0] or board[x][y][1][1] or board[x][y][0][1]:
            return True
    return False


def solution(n, build_frame):
    answer = []
    board = [[[[0, 0], [0, 0]] for _ in range(n + 1)] for _ in range(n + 1)]
    orders = {}
    for bf in build_frame:
        y, x, a, b = bf
        if b:
            x = n - x
            if a:  # 보
                if isbuild(board, bf, n):
                    board[x][y][a][0], board[x][y + 1][a][1] = 1, 1
                    orders[tuple(bf)] = 1
            else:  # 기둥
                if isbuild(board, bf, n):
                    board[x][y][a][0], board[x - 1][y][a][1] = 1, 1
                    orders[tuple(bf)] = 1
        else:
            tx, tb = n - x, 1
            orders.pop((y, x, a, tb))
            if a:
                board[tx][y][a][0], board[tx][y + 1][a][1] = 0, 0
            else:
                board[tx][y][a][0], board[tx - 1][y][a][1] = 0, 0
            for order in orders:
                if isbuild(board, order, n):
                    continue
                else:
                    orders[(y, x, a, tb)] = 1
                    if a:
                        board[tx][y][a][0], board[tx][y + 1][a][1] = 1, 1
                    else:
                        board[tx][y][a][0], board[tx - 1][y][a][1] = 1, 1
                    break
    for order in orders:
        answer.append(order[:3])
    answer.sort()

    return answer