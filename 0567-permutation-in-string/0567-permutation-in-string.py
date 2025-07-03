class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(len1):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        for i in range(len1, len2):
            count_s2[ord(s2[i]) - ord('a')] += 1
            count_s2[ord(s2[i - len1]) - ord('a')] -= 1

            if count_s1 == count_s2:
                return True

        return False
