class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False
        
        s_t, t_s  = {}, {}

        for i in range(len(s)):

            if s[i] not in s_t:
                s_t[s[i]] = i
            if t[i] not in t_s:
                t_s[t[i]] = i

            if s_t[s[i]] != t_s[t[i]]:
                return False
        return True


         

        

        