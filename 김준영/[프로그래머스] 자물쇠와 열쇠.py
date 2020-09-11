def rotate(key):
    n = len(key)
    rkey = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rkey[j][n-1-i] = key[i][j]
    return rkey

def isanswer(board, key, x, y, m, hall):
    cnt = 0
    for i in range(m):
        for j in range(m):
            if board[x+i][y+j] == 1 and key[i][j] == 1:
                return False
            elif board[x+i][y+j] == 2 and key[i][j] == 1:
                cnt += 1
    if cnt == hall:
        return True
    return False


def solution(key, lock):
    n = len(lock) + (len(key)-1) * 2
    m = len(key)
    board = [[0 for _ in range(n)] for _ in range(n)]
    hall = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                hall += 1
                lock[i][j] = 2

    for i in range(m-1, m+len(lock)-1):
        for j in range(m-1, m+len(lock)-1):
            board[i][j] = lock[i-m+1][j-m+1]

    for _ in range(4):
        for i in range(n-(m-1)):
            for j in range(n-(m-1)):
                if isanswer(board, key, i, j, m, hall):
                    return True
        key = rotate(key)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))