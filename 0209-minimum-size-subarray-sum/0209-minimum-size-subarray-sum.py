class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        minLen = n + 1
        sumArr = start = 0

        for end, value in enumerate(nums):
            sumArr += value

            while start < n and sumArr >= target:
                minLen = min(minLen, end-start+1)
                sumArr -= nums[start]
                start += 1
        if minLen <= n:
           return minLen 

        else:
            return 0
