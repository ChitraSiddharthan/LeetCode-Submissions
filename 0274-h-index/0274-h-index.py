class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0

        while h < len(citations) and citations[h] >= h+1:
            h += 1
        return h
        