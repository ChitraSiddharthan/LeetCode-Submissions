class Solution(object):
    def generate(self, numRows):
        def get_row(n):
            if n == 0:
                return [1]
            prev = get_row(n-1)
            row = [1]
            for i in range(1, n):
                row.append(prev[i-1] + prev[i])
            row.append(1)
            return row
        
        return [get_row(i) for i in range(numRows)]
        