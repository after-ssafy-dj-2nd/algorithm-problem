def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        tmp = ''
        limit = 0
        for j in range(0, len(s), i):
            if j < limit:
                continue
            cnt = 0
            cur = s[j:j+i]
            for k in range(j, len(s), i):
                make = s[k:k+i]
                if make == cur:
                    cnt += 1
                    if k+i >= len(s):
                        limit = len(s) + 1
                        break
                else:
                    limit = k
                    break
            if cnt == 1:
                tmp += cur
            elif cnt > 1:
                tmp += str(cnt) + cur
        if len(tmp) < answer:
            answer = len(tmp)
    return answer