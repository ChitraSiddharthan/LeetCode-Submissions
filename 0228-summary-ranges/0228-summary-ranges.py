class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        start = None

        for i, num in enumerate(nums):
            if start is None:
                start = num
            
            if i + 1 < len(nums) and num + 1 == nums[i + 1]:
                continue
            elif start == num:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(num))
            start = None
        return ranges

        