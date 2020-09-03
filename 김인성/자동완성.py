def auto(dic):
    global ans
    for string in dic:
        num, next = dic[string]
        ans += num
        if num != 1:
            auto(next)


def solution(words):
    global ans
    trie = {}
    for word in words:
        now = trie
        for string in word:
            if not now.get(string):
                now.update({string: [1, {}]})
            else:
                now[string][0] += 1
            now = now[string][1]
    ans = 0
    auto(trie)
    return ans