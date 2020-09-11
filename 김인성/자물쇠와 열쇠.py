def rotate(key):
    m = len(key)
    board = [[0] * m for _ in range(m)]
    for j in range(m):
        for i in range(m):
            board[j][i] = key[m - i - 1][j]
    return board


def is_ok(key, lock, k, l):
    m, n = len(key), len(lock)
    for j in range(n):
        for i in range(n):
            if 0 <= j - k < m and 0 <= i - l < m:
                if not lock[j][i] ^ key[j-k][i-l]:
                    return False
            else:
                if not lock[j][i]:
                    return False
    return True



def solution(key, lock):
    m, n = len(key), len(lock)
    for _ in range(4):
        for k in range(-n+1, n):
            for l in range(-n, n):
                if is_ok(key, lock, k, l):
                    return True
        key = rotate(key)
    return False