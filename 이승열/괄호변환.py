def wordsplit(w):
    tmp = 0
    if w:
        for i in range(len(w)):
            if w[i] == '(':
                tmp += 1
            else:
                tmp -= 1
            if not tmp:
                break
        u, v = w[:i+1],w[i+1:]
        print(u,v)
        if correct(u):
            return u + wordsplit(v)
        else:
            return '(' + wordsplit(v) + ')' + u[1:-1][::-1]
    else:
        return ''
    
def correct(w):
    tmp = 0
    for i in range(len(w)):
        if tmp < 0:
            return False
        if w[i] == '(':
            tmp += 1
        else:
            tmp -= 1
    return True

def solution(p):
    return wordsplit(p)