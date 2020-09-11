def solution(record):
    user = {}
    logs = []
    for string in record:
        string = list(string.split())
        if string[0] == "Enter":
            user[string[1]] = string[2]
            logs.append((0, string[1]))
        elif string[0] == "Leave":
            logs.append((1, string[1]))
        else:
            user[string[1]] = string[2]
    result = []
    for cmd, u_id in logs:
        if cmd:
            result.append('{}님이 나갔습니다.'.format(user[u_id]))
        else:
            result.append('{}님이 들어왔습니다.'.format(user[u_id]))
    return result