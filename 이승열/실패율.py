def solution(N, stages):
    success = [0] * (N+1)
    for stage in stages:
        for i in range(stage):
            success[i] += 1
    fail = [0] * N
    for i in range(N):
        fail[i] = (success[i] - success[i+1]) / success[i] if success[i] else 0
    answer = sorted(range(N), key = lambda i : -fail[i])
    return list(map(lambda x : x+1,answer))