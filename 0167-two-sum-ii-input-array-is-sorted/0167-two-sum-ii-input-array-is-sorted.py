class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers [r]

            if sum == target:
                return[l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        return []
             
               