class Solution(object):
    def twoSum(self, nums, target):
        sumMap = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in sumMap:
                return [sumMap[complement], i]
            sumMap[n] = i
        return []
        