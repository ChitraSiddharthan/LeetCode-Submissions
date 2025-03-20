class Solution(object):
    def longestCommonPrefix(self, strs):
        
        strs.sort()

        first_string = strs[0]
        last_string = strs[-1]
        min_len = min(len(first_string), len(last_string))

        i = 0
        while i < min_len and first_string[i] == last_string[i]:
              i += 1
        return first_string[:i]



        