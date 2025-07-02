class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(b, e): #b: base, e: exponent
            if e == 0:
                return 1.0
            half = fast_pow(b, e // 2)
            if e % 2 == 0:
                return half * half
            else:
                return half * half * b
            
        if n < 0:
            x = 1/x
            n = -n
        
        return fast_pow(x,n)
            
