dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    def find_black(location):
        global ans
        for num, spots in location.items():
            mapping = {}
            tmp = []
            for x0, y0 in spots:
                for k in range(4):
                    for m in range(1, 3):
                        x, y = x0 + m*dx[k], y0 + m*dy[k]
                        if 0 <= x < n and 0 <= y < n and not board[y][x]:
                            if mapping.get((x, y)):
                                tmp.append((x, y))
                            else:
                                mapping.update({(x, y): 1})
                        else:
                            break
            if len(tmp) >= 2:
                flag = False
                for x, y in tmp:
                    while y > 0 and not flag:
                        y -= 1
                        if board[y][x]:
                            flag = True
                            break
                if flag:
                    continue
                else:
                    ans += 1
                    for x, y in location.pop(num):
                        board[y][x] = 0
                    return find_black(location)
        else:
            return

    global ans
    ans = 0
    n = len(board)
    block = {}
    for j in range(n):
        for i in range(n):
            if board[j][i]:
                num = board[j][i]
                if block.get(num):
                    block[num].append((i, j))
                else:
                    block.update({num: [(i, j)]})
    find_black(block)
    return ans
