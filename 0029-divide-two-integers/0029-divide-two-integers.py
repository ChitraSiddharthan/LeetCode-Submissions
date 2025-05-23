class Solution(object):
    def divide(self, dividend, divisor):
        Max = 2**31 - 1
        Min = -2**31

        if dividend == Min and divisor == -1:
            return Max
        
        negative = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient        