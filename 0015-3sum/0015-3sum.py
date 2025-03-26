class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()     
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            p1, p2 = i+1, n-1

            while p1 < p2:
                finalSum = nums[i] + nums[p1] + nums[p2]

                if finalSum == 0:
                    result.append([nums[i], nums[p1], nums[p2]])

                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    
                    p1 += 1
                    p2 -= 1
                
                elif finalSum < 0:
                    p1 += 1
                
                else:
                    p2 -= 1
        
        return result


            
        