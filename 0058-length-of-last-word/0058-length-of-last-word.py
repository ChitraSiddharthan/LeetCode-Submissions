class Solution(object):
    def lengthOfLastWord(self, s):
        l = 0

        string = s.strip()

        for i in range(len(string)):
            if string[i] == " ":
                l = 0
            else:
                l += 1
        return l
        