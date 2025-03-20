class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for char in strs:
            sorted_char = ''.join(sorted(char))
            result[sorted_char].append(char)
        return list(result.values())
        