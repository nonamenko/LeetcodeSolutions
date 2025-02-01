class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[0][i] = 1
        ri = rj = 0
        for i in range(1, len(s)):
            for j in range(i, len(s)):
                if s[j] == s[j - i]:
                    dp[i][j] = dp[max(0, i-2)][j-1]
                    if dp[i][j] == 1:
                        ri = i
                        rj = j
        return s[rj-ri:rj+1]
