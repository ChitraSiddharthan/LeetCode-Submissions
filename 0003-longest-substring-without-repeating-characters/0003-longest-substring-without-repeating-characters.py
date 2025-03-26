class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            result = max(result, len(charSet))
        return result
        