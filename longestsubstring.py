from collections import Counter


def LongestSubstring(s):
    char = Counter()
    left = right = 0
    res = 0
    while right < len(s):
        r = s[right]
        char[r]+=1
        while char[r] > 1:
            l = s[left]
            char[l] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

s= 'abcabcbb'
print(LongestSubstring(s))