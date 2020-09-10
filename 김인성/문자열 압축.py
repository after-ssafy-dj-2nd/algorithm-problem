def solution(s):
    ans = n = len(s)
    for k in range(1, n-1):
        tmp_ans = 0
        prv_string = s[:k]
        string_cnt = 0
        for i in range(k, n, k):
            if prv_string == s[i:i+k]:
                string_cnt += 1
            else:
                tmp_ans += k + (len(str(string_cnt+1)) if string_cnt else 0)
                prv_string, string_cnt = s[i:i+k], 0
        else:
            tmp_ans += (len(str(string_cnt + 1)) if string_cnt else 0) + n - i
        ans = min(ans, tmp_ans)
    return ans