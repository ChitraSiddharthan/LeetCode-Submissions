class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self.encode(result)
        return result

    def encode(self, s: str) -> str:
        encoded = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            encoded += str(count) + s[i]
            i += 1
        return encoded
