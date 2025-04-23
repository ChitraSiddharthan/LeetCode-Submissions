class Solution(object):
    def calculate(self, s):
        result = 0
        num = 0
        operator = 1
        stack = [1]

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += operator * num
                operator = stack[-1]
                num = 0
            elif char == '-':
                result += operator * num
                operator = -stack[-1]
                num = 0
            elif char == '(':
                stack.append(operator)
            elif char == ')':
                stack.pop()
        
        return result + operator * num
        