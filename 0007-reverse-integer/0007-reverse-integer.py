class Solution(object):
    def reverse(self, x):
        
        reverse = 0
        maxInt = 2**31 - 1
        minInt = -2**31

        while x:
            if reverse < minInt // 10 + 1 or reverse > maxInt // 10:
                return 0
            digit = x % 10
            
            if x < 0 and digit > 0:
                    digit -= 10
                
            reverse = reverse * 10 + digit
            x = (x - digit) // 10
        
        return reverse
            

        