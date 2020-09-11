def solution(words, queries):
    index = [([0, {}], [0, {}]) for _ in range(10001)]
    for word in words:
        n = len(word)
        trie, reversed_trie = index[n]
        for i in range(len(word)):
            key1, key2 = word[i], word[n-i-1]
            trie[0] += 1
            reversed_trie[0] += 1
            if not trie[1].get(key1):
                trie[1][key1] = [0, {}]
            if not reversed_trie[1].get(key2):
                reversed_trie[1][key2] = [0, {}]
            trie = trie[1][key1]
            reversed_trie = reversed_trie[1][key2]
    ans = []
    for query in queries:
        if query[0] == "?":
            trie = index[len(query)][1]
            query = query[::-1]
        else:
            trie = index[len(query)][0]
        for char in query:
            if char == "?":
                ans.append(trie[0])
                break
            else:
                try:
                    trie = trie[1][char]
                except KeyError:
                    ans.append(0)
                    break
        else:
            ans.append(trie[0])
    return ans