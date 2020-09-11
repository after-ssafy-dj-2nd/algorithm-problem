from itertools import combinations
def has_subset(used, indexes):
    indexes = set(indexes)
    for used_hash in used:
        if used_hash.issubset(indexes):
            return True
    return False


def solution(relation):
    n = len(relation[0])
    used = []
    ans = 0
    for i in range(1, n+1):
        com = combinations([i for i in range(n)], i)
        for indexes in com:
            if not has_subset(used, indexes):
                tmp = {}
                for col in relation:
                    key = tuple([col[idx] for idx in indexes])
                    if tmp.get(key):
                        break
                    else:
                        tmp[key] = True
                else:
                    ans += 1
                    used.append(set(indexes))
    return ans