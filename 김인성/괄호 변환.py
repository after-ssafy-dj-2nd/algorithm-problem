def solution(p):
    counter = 0
    if not p:
        return ''
    for i in range(len(p)):
        counter += 1 if p[i] == "(" else -1
        if not counter:
            u, v = p[:i + 1], p[i + 1:]
            break
    return u + solution(v) if not u or u[0] == "(" else "(" + solution(v) + ")" + ''.join([")" if i == "(" else "(" for i in u[1:-1]])