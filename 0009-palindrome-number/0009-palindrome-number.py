class Solution(object):
    def isPalindrome(self, x):
        reverse = 0
        temp = x

        while(temp > 0):
             last = temp % 10
             reverse = reverse * 10 + last
             temp = temp // 10

        return x==reverse
        
        