class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if merged[-1][1] < start:
                merged.append([start, end])
            else:        
                merged[-1][1] = max(merged[-1][1], end)
        return merged