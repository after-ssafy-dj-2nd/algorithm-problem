def solution(record):
    user = {}
    tmp = []
    answer = []
    for log in record:
        data = log.split(' ')
        if data[0] =='Change':
            user[data[1]]=data[2]
        elif data[0] == 'Enter':
            tmp.append((data[1], '님이 들어왔습니다.'))
            user[data[1]]=data[2]
        elif data[0] =='Leave':
            tmp.append((data[1], '님이 나갔습니다.'))
    for t in tmp:
        answer.append(user[t[0]] + t[1])
    return answer