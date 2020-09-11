from heapq import heappush, heappop

def solution(N, stages):
    people = len(stages)
    dp = [0] * N
    for stage in stages:
        if stage <= N:
            dp[stage-1] += 1
    heap = []
    for i in range(N):
        if people:
            heappush(heap, (-dp[i] / people, i + 1))
            people -= dp[i]
        else:
            heappush(heap, (0, i + 1))
    result = []
    while heap:
        _, idx = heappop(heap)
        result.append(idx)
    return result