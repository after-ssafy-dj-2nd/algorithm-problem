# () 개수가 같다면 균형잡힌 괄호 문자열
# ()의 괄호의 짝도 맞으면 올바른 괄호 문자열
def solution(p):
    answer = solve(p)
    return answer

def isproper(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        elif p[i] == ')':
            if stack:
                stack.pop()
            else:
                return False
    return True

def solve(p):
    if not p:
        return p
    l, r = 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == ')':
            u += p[i]
            r += 1
        else:
            u += p[i]
            l += 1
        if r == l:
            v = p[i+1:]
            break
    if isproper(u):
        return u + solve(v)
    else:
        text = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                text += ')'
            else:
                text += '('
        return '('+ solve(v) + ')' + text
solution(')(')