class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        counter = Counter()
        i = j = 0
        while (j < len(s)):
            while (j < len(s)):
                counter[s[j]] += 1
                if counter[s[j]] == 2:
                    break
                j += 1
            res = max(res, j - i)
            while (i < j):
                counter[s[i]] -= 1
                if counter[s[i]] == 1:
                    break
                i += 1
            j += 1
            i += 1
        return res