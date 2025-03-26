class Solution(object):
    def productExceptSelf(self, nums):
        elem = len(nums)
        arr = [1]*elem

        prefixProd = 1
        for i in range(elem):
            arr[i] = prefixProd
            prefixProd *= nums[i]

        suffixProd = 1
        for i in range(elem-1, -1, -1):
            arr[i] *= suffixProd
            suffixProd *= nums[i]
        
        return arr

        