class Solution(object):
    def longestConsecutive(self, nums):
        
        ConMap = defaultdict(int)
        result = 0

        for num in nums:
            if not ConMap[num]:
                ConMap[num] = ConMap[num - 1] + ConMap[num + 1] + 1
                ConMap[num - ConMap[num - 1]] = ConMap[num]
                ConMap[num + ConMap[num + 1]] = ConMap[num]
                result = max(result, ConMap[num])
        return result
        