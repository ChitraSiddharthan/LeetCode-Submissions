class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(nums, 0)
        return self.result
    
    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.result.append(nums[:])
            return
        
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]

        