def solution(n, build_frame):
    def can_construct(x, y, a):
        if a:
            if (board.get((x - 1, y, 1)) and board.get((x + 1, y, 1))) or board.get((x, y - 1, 0)) or board.get(
                    (x + 1, y - 1, 0)):
                return True
        else:
            if not y or board.get((x, y - 1, 0)) or board.get((x - 1, y, 1)) or board.get((x, y, 1)):
                return True
        return False

    board = {}
    for x, y, a, b in build_frame:
        if b:
            if can_construct(x, y, a):
                board.update({(x, y, a): 1})
        else:
            board.pop((x, y, a))
            for x0, y0, a0 in board:
                if not can_construct(x0, y0, a0):
                    board.update({(x, y, a): 1})
                    break
    return list(sorted(map(list, board.keys())))
