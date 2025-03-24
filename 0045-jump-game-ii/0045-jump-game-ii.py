class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        
        jumpCount = 0
        maxIndex = 0
        lastIndex = 0

        for i in range(n-1):
            maxIndex = max(maxIndex, i + nums[i])

            if i == lastIndex:
                jumpCount += 1
                lastIndex = maxIndex

                if lastIndex >= n-1:

                    return jumpCount
        
        return jumpCount

        