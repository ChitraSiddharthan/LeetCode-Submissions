class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        rev_words = ""

        for word in reversed(words):
            rev_words += word + " "
        rev_words = rev_words.strip()
        return rev_words

        