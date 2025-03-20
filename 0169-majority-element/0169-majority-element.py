class Solution(object):
    def majorityElement(self, nums):
        
        elem = 0
        count = 0

        for i in nums:
            if count == 0:
                elem  = i
            if i == elem:
                count += 1 
            else:
                count -= 1
        count = 0

        for i in nums:
            if i == elem:
                count += 1
        return elem if count>(len(nums)//2) else -1

        