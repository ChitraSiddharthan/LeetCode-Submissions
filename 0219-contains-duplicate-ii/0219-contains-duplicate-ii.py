class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        duplicate = {}

        for i, num in enumerate(nums):
            if num in duplicate and i - duplicate[num] <= k:
                return True
            duplicate[num] = i
        return False
        