class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for char, count in r_count.items():
            if m_count[char] < count:
                return False
        return True
        
        