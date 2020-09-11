def distance(a,b,n):
    if a < b:
        return min(b-a,n+a-b)
    else:
        return min(a-b,n-a+b)
def solution(n, weak, dist):
    min_distance = []
    for i in range(len(weak)):
        min_distance.append(distance(weak[i],weak[i-1],n))
    min_distance = sorted(min_distance)
    result = 0
    for j in range(len(dist)):
        result += min_distance.pop() + dist.pop()
        if result >= n:
            return j+1
    return -1