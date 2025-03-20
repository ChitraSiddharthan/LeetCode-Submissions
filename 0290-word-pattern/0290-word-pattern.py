class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()

        if len(pattern) != len(s):
            return False
        
        pattern_s = {}
        s_pattern = {}

        for char, word in zip(pattern, s):
            if char in pattern_s and pattern_s[char] != word:
                return False
            if word in s_pattern and s_pattern[word] != char:
                return False
            pattern_s[char] = word
            s_pattern[word] = char
        
        return True
        
        