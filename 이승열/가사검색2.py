def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        start, end = 0,len(query)
        if query[0] == '?':
            for i in range(end):
                if query[i] != '?':
                    start = i
                    break
            else:
                start = end
        else:
            for i in range(end-1,-1,-1):
                if query[i] != '?':
                    end = i+1
                    break
        for word in words:
            if len(word)==len(query) and word[start:end] == query[start:end]:
                count += 1
        answer.append(count)
    return answer