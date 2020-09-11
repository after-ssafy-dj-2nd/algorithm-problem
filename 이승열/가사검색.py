def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        for word in words:
            if len(query) == len(word):
                for i in range(len(word)):
                    if query[i] == '?':
						pass
					elif query[i] == word[i]:
						pass
					else:
						break
                else:
                    count += 1
        answer.append(count)
    return answer