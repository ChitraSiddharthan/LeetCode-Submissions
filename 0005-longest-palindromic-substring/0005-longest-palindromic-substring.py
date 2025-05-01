class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        temp = [[True] * n for _ in range(n)]
        start = 0
        maxLen = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                temp[i][j] = False

                if s[i] == s[j] and temp[i+1][j-1]:
                    temp[i][j] = True

                    if maxLen < j - i + 1:
                        start = i
                        maxLen = j - i + 1
        return s[start : start + maxLen]
