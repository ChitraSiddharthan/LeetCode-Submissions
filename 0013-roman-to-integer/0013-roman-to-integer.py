class Solution(object):
    def romanToInt(self, s):
        n = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
         
        res = 0

        for i in range(len(s)):
            if i+1 < len(s) and n[s[i]] < n[s[i+1]]:
                res -= n[s[i]]
            else:
                res += n[s[i]]
        return res
        