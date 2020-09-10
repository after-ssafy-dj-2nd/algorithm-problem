import sys

sys.setrecursionlimit(100001)


def dfs(query, trie, n, t):
    answer = 0
    if t == n:
        return trie['remain'][n - t]
    if query[t] == '?':
        if n - t in trie['remain']:
            return trie['remain'][n - t]
        else:
            return 0


    else:
        if query[t] in trie:
            answer += dfs(query, trie[query[t]], n, t + 1)

    return answer


def solution(words, queries):
    answer = []
    dictionary = dict({'remain': {}})
    rdictionary = dict({'remain': {}})

    for word in words:
        cur = dictionary
        for idx, ch in enumerate(word):
            if ch in cur:
                if len(word) - idx in cur['remain']:
                    cur['remain'][len(word) - idx] += 1
                else:
                    cur['remain'][len(word) - idx] = 1
                cur = cur[ch]
            else:
                if len(word) - idx in cur['remain']:
                    cur['remain'][len(word) - idx] += 1
                else:
                    cur['remain'][len(word) - idx] = 1
                cur[ch] = {'remain': {}}
                cur = cur[ch]
        if 0 in cur['remain']:
            cur['remain'][0] += 1
        else:
            cur['remain'][0] = 1
        cur = rdictionary
        for idx, ch in enumerate(word[::-1]):
            if ch in cur:
                if len(word) - idx in cur['remain']:
                    cur['remain'][len(word) - idx] += 1
                else:
                    cur['remain'][len(word) - idx] = 1
                cur = cur[ch]
            else:
                if len(word) - idx in cur['remain']:
                    cur['remain'][len(word) - idx] += 1
                else:
                    cur['remain'][len(word) - idx] = 1
                cur[ch] = {'remain': {}}
                cur = cur[ch]
        if 0 in cur['remain']:
            cur['remain'][0] += 1
        else:
            cur['remain'][0] = 1
    for query in queries:
        if query[0] == '?':
            answer.append(dfs(query[::-1], rdictionary, len(query), 0))
        else:
            answer.append(dfs(query, dictionary, len(query), 0))
    return answer