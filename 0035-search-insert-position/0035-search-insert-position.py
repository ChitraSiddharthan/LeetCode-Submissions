class Solution(object):
    def searchInsert(self, nums, target):
        m, n = 0, len(nums) - 1

        while m <= n:
          mid = (m + n) // 2

          if nums[mid] == target:
            return mid
          elif nums[mid] < target:
            m = mid + 1
          else:
            n = mid - 1
        
        return m
        
        