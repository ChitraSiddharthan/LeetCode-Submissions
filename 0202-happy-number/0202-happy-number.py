class Solution(object):
    def isHappy(self, n):
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False

    def sumOfSquare(self, n):
        square = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            square += digit
            n = n // 10
        return square
            
        