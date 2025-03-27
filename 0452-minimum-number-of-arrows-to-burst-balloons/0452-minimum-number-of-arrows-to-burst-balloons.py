class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda x: x[1])
        arrow = 1
        initialPosition = points[0][1]

        for start, end in points:
            if start > initialPosition:
                arrow += 1
                initialPosition = end
        
        return arrow