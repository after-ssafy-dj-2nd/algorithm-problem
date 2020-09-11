def solution(p):
    answer = ''
    tmp = 0
    for i in p:
        if i == '(':
            if tmp < 0:
                answer+= ')'
            else:
                answer+= '('
            tmp += 1
        else:
            if tmp > 0:
                answer += ')'
            else:
                answer += '('
            tmp -= 1
    return answer