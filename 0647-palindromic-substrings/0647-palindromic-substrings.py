class Solution(object):
    def countSubstrings(self, s):
        def extendPalindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        result = 0
        for i in range(len(s)):
            result += extendPalindrome(i, i)
            result += extendPalindrome(i, i+1)
        return result

          