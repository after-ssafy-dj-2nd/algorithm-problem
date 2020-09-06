from sys import setrecursionlimit

setrecursionlimit(10000)

def find(string, num, trie, idx):
    if string[idx] == "?":
        return num
    if trie.get(string[idx]):
        return find(string, trie[string[idx]][0], trie[string[idx]][1], idx+1)
    else:
        return 0

def solution(words, queries):
    answer = []
    tries, tries_reversed = [{} for _ in range(100001)], [{} for _ in range(100001)]
    for word in words:
        n = len(word)
        now, now_reversed = tries[n-1], tries_reversed[n-1]
        for i in range(n):
            if not now.get(word[i]):
                now.update({word[i]: [1, {}]})
            else:
                now[word[i]][0] += 1
            now = now[word[i]][1]
            if not now_reversed.get(word[n-i-1]):
                now_reversed.update({word[n-i-1]: [1, {}]})
            else:
                now_reversed[word[n-i-1]][0] += 1
            now_reversed = now_reversed[word[n-i-1]][1]
    for query in queries:
        n = len(query)
        if query[0] == "?":
            now = tries_reversed[n-1]
            query = query[::-1]
        else:
            now = tries[n-1]
        if query[0] == "?":
            tmp = 0
            for num, _ in now.values():
                tmp += num
            else:
                answer.append(tmp)
        else:
            if now.get(query[0]):
                now = now[query[0]]
                answer.append(find(query, now[0], now[1], 1))
            else:
                answer.append(0)
    return answer



print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))