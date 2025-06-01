class Solution(object):
    def grayCode(self, n):
        result = []
        for i in range(1 << n):
            result.append(i^(i >> 1))
        return result
        