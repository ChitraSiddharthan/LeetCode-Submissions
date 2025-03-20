class Solution(object):
    def isPalindrome(self, s):
        first_char, last_char = 0, len(s)-1

        while first_char < last_char:
    
            while first_char < last_char and not s[first_char].isalnum():
                first_char += 1
            while first_char < last_char and not s[last_char].isalnum():
                last_char -= 1

            
            if s[first_char].lower() != s[last_char].lower():
                return False

            first_char += 1
            last_char -= 1

        return True